"""
Main driver file.
Handling user input.
Displaying current GameState object.
"""
import pygame as p
import ChessEngine, ChessAI
import sys
from multiprocessing import Process, Queue
import requests as r

BASE = "http://localhost:5000"
BOARD_WIDTH = BOARD_HEIGHT = 512
MOVE_LOG_PANEL_WIDTH = 250
MOVE_LOG_PANEL_HEIGHT = BOARD_HEIGHT
DIMENSION = 8
SQUARE_SIZE = BOARD_HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

nickname = input("Enter a nickname : ")
response = r.put(BASE + "/info/nickname", {"nickname": nickname})
colour = response.json()["colour"]

def loadImages():
    """
    Initialize a global directory of images.
    This will be called exactly once in the main.
    """
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQUARE_SIZE, SQUARE_SIZE))


def main():
    """
    The main driver for our code.
    This will handle user input and updating the graphics.
    """
    p.init()
    screen = p.display.set_mode((BOARD_WIDTH + MOVE_LOG_PANEL_WIDTH, BOARD_HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    move_made = False  # flag variable for when a move is made
    animate = False  # flag variable for when we should animate a move
    loadImages()  # do this only once before while loop
    running = True
    square_selected = ()  # no square is selected initially, this will keep track of the last click of the user (tuple(row,col))
    player_clicks = []  # this will keep track of player clicks (two tuples)
    game_over = False
    ai_thinking = False
    move_undone = False
    move_finder_process = None
    move_log_font = p.font.SysFont("Arial", 14, False, False)
    player_one = True  # if a human is playing white, then this will be True, else False
    player_two = True  # if a human is playing white, then this will be True, else False

    while running:
        # human_turn = (game_state.white_to_move and player_one) or (not game_state.white_to_move and player_two)

        response = r.get(BASE + "/info/white_to_move")
        white_to_move = response.json()["white_to_move"]

        turn_to_move = (colour == "white") and white_to_move

        response = r.get(BASE + "/board")
        board = response.json()

        for e in p.event.get():
            if e.type == p.QUIT:
                r.post(BASE + "/info/close_game", {"nickname": nickname})
                p.quit()
                sys.exit()
            # mouse handler
            elif e.type == p.MOUSEBUTTONDOWN:
                if not game_over:
                    location = p.mouse.get_pos()  # (x, y) location of the mouse
                    col = location[0] // SQUARE_SIZE
                    row = location[1] // SQUARE_SIZE
                    if square_selected == (row, col) or col >= 8:  # user clicked the same square twice
                        square_selected = ()  # deselect
                        player_clicks = []  # clear clicks
                    else:
                        square_selected = (row, col)
                        player_clicks.append(square_selected)  # append for both 1st and 2nd click
                    if len(player_clicks) == 2 and turn_to_move:  # after 2nd click

                        response = r.put(BASE + "/moves/makemove", {"startrow": player_clicks[0][0], "startcol": player_clicks[0][1], "endrow": player_clicks[1][0], "endcol": player_clicks[1][1]})
                        move_made = response.json()["move_made"]
                        animate = True
                        square_selected = ()  # reset user clicks
                        player_clicks = []

                        if not move_made:
                            player_clicks = [square_selected]

            # key handler
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:  # undo when 'z' is pressed
                    response = r.put(BASE + "/moves/undomove")
                    # move_undone = response.json()["move_undone"]
                    move_made = True
                    animate = False
                    game_over = False
                    if ai_thinking:
                        move_finder_process.terminate()
                        ai_thinking = False
                    move_undone = True
                if e.key == p.K_r:  # reset the game when 'r' is pressed
                    response = r.post(BASE + "/reset_game")
                    square_selected = ()
                    player_clicks = []
                    move_made = False
                    animate = False
                    game_over = False
                    if ai_thinking:
                        move_finder_process.terminate()
                        ai_thinking = False
                    move_undone = True

        # AI move finder
        # if not game_over and not human_turn and not move_undone:
        #     if not ai_thinking:
        #         ai_thinking = True
        #         return_queue = Queue()  # used to pass data between threads
        #         move_finder_process = Process(target=ChessAI.findBestMove, args=(game_state, valid_moves, return_queue))
        #         move_finder_process.start()
        #
        #     if not move_finder_process.is_alive():
        #         ai_move = return_queue.get()
        #         if ai_move is None:
        #             ai_move = ChessAI.findRandomMove(valid_moves)
        #         game_state.makeMove(ai_move)
        #         move_made = True
        #         animate = True
        #         ai_thinking = False

        if move_made:
            if animate:
                animateMove(screen, clock)
            move_made = False
            animate = False
            move_undone = False

        drawGameState(screen, square_selected)

        if not game_over:
            drawMoveLog(screen, move_log_font)

        response = r.get(BASE + "/info/checkmate")
        checkmate = response.json()["checkmate"]

        response = r.get(BASE + "/info/stalemate")
        stalemate = response.json()["stalemate"]

        response = r.get(BASE + "/info/white_to_move")
        white_to_move = response.json()["white_to_move"]

        if checkmate:
            game_over = True
            if white_to_move:
                drawEndGameText(screen, "Black wins by checkmate")
            else:
                drawEndGameText(screen, "White wins by checkmate")

        elif stalemate:
            game_over = True
            drawEndGameText(screen, "Stalemate")

        clock.tick(MAX_FPS)
        p.display.flip()


def drawGameState(screen, square_selected):
    """
    Responsible for all the graphics within current game state.
    """

    response = r.get(BASE + "/board")
    board = response.json()

    drawBoard(screen)  # draw squares on the board
    highlightSquares(screen, square_selected)
    drawPieces(screen, board)  # draw pieces on top of those squares


def drawBoard(screen):
    """
    Draw the squares on the board.
    The top left square is always light.
    """
    global colors
    colors = [p.Color("white"), p.Color("gray")]
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            color = colors[((row + column) % 2)]
            p.draw.rect(screen, color, p.Rect(column * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def highlightSquares(screen, square_selected):
    """
    Highlight square selected and moves for piece selected.
    """

    response = r.get(BASE + "/visuals/highlight")
    data = response.json()

    if "message" not in data:
        s = p.Surface((SQUARE_SIZE, SQUARE_SIZE))
        s.set_alpha(100)
        s.fill(p.Color('green'))
        screen.blit(s, (data["last_move"]["end_col"] * SQUARE_SIZE, data["last_move"]["end_row"] * SQUARE_SIZE))
    if square_selected != ():
        row, col = square_selected
        if data["board"][row][col][0] == (
                'w' if data["white_to_move"] else 'b'):  # square_selected is a piece that can be moved
            # highlight selected square
            s = p.Surface((SQUARE_SIZE, SQUARE_SIZE))
            s.set_alpha(100)  # transparency value 0 -> transparent, 255 -> opaque
            s.fill(p.Color('blue'))
            screen.blit(s, (col * SQUARE_SIZE, row * SQUARE_SIZE))
            # highlight moves from that square
            s.fill(p.Color('yellow'))
            for move in data["valid_move_coords"]:
                if move[0][0] == row and move[0][1] == col:
                    screen.blit(s, (move[1][1] * SQUARE_SIZE, move[1][0] * SQUARE_SIZE))


def drawPieces(screen, board):
    """
    Draw the pieces on the board using the current game_state.board
    """
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            piece = board[row][column]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(column * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def drawMoveLog(screen, font):
    """
    Draws the move log.
    """
    move_log_rect = p.Rect(BOARD_WIDTH, 0, MOVE_LOG_PANEL_WIDTH, MOVE_LOG_PANEL_HEIGHT)
    p.draw.rect(screen, p.Color('black'), move_log_rect)

    response = r.get(BASE + "/visuals/movelog")
    move_texts = response.json()

    if "message" not in move_texts:

        moves_per_row = 3
        padding = 5
        line_spacing = 2
        text_y = padding
        for i in range(0, len(move_texts), moves_per_row):
            text = ""
            for j in range(moves_per_row):
                if i + j < len(move_texts):
                    text += move_texts[i + j]

            text_object = font.render(text, True, p.Color('white'))
            text_location = move_log_rect.move(padding, text_y)
            screen.blit(text_object, text_location)
            text_y += text_object.get_height() + line_spacing


def drawEndGameText(screen, text):
    font = p.font.SysFont("Helvetica", 32, True, False)
    text_object = font.render(text, False, p.Color("gray"))
    text_location = p.Rect(0, 0, BOARD_WIDTH, BOARD_HEIGHT).move(BOARD_WIDTH / 2 - text_object.get_width() / 2,
                                                                 BOARD_HEIGHT / 2 - text_object.get_height() / 2)
    screen.blit(text_object, text_location)
    text_object = font.render(text, False, p.Color('black'))
    screen.blit(text_object, text_location.move(2, 2))


def animateMove(screen, clock):
    """
    Animating a move
    """

    response = r.get(BASE + "/visuals/animate")
    data = response.json()

    global colors
    d_row = data["last_move"]["end_row"] - data["last_move"]["start_row"]
    d_col = data["last_move"]["end_col"] - data["last_move"]["start_col"]
    frames_per_square = 10  # frames to move one square
    frame_count = (abs(d_row) + abs(d_col)) * frames_per_square
    for frame in range(frame_count + 1):
        row, col = (data['last_move']['start_row'] + d_row * frame / frame_count, data['last_move']['start_col'] + d_col * frame / frame_count)
        drawBoard(screen)
        drawPieces(screen, data["board"])
        # erase the piece moved from its ending square
        color = colors[(data['last_move']['end_row'] + data['last_move']['end_col']) % 2]
        end_square = p.Rect(data['last_move']['end_col'] * SQUARE_SIZE, data['last_move']['end_row'] * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
        p.draw.rect(screen, color, end_square)
        # draw captured piece onto rectangle
        if data['last_move']["piece_captured"] != '--':
            if data['last_move']["is_enpassant"]:
                enpassant_row = data['last_move']['end_row'] + 1 if data['last_move']["piece_captured"][0] == 'b' else data['last_move']['end_row'] - 1
                end_square = p.Rect(data['last_move']['end_col'] * SQUARE_SIZE, enpassant_row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            screen.blit(IMAGES[data['last_move']["piece_captured"]], end_square)
        # draw moving piece
        screen.blit(IMAGES[data['last_move']["piece_moved"]], p.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        p.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()