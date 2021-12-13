"""
This is the client that pulls the board from chessapi.py
"""

import pygame as p
import requests
import time as t

nickname = input("Enter a nickname --> ")

BASE = "http://127.0.0.1:5000/"

WIDTH = HEIGHT = 512  # 400 would also work
DIMENSION = 8  # dimensions of a chess board are 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15  # for animations later on
IMAGES = {}
player_is_white = None


def load_images():
    pieces = ["wP", "wR", "wN", "wB", "wQ", "wK", "bP", "bR", "bN", "bB", "bQ", "bK"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


def swap_clicks(a, b):
    swapped = []
    if a == 0:
        swapped.append(7)
    elif a == 1:
        swapped.append(6)
    elif a == 2:
        swapped.append(5)
    elif a == 3:
        swapped.append(4)
    elif a == 4:
        swapped.append(3)
    elif a == 5:
        swapped.append(2)
    elif a == 6:
        swapped.append(1)
    elif a == 7:
        swapped.append(0)
    if b == 0:
        swapped.append(7)
    elif b == 1:
        swapped.append(6)
    elif b == 2:
        swapped.append(5)
    elif b == 3:
        swapped.append(4)
    elif b == 4:
        swapped.append(3)
    elif b == 5:
        swapped.append(2)
    elif b == 6:
        swapped.append(1)
    elif b == 7:
        swapped.append(0)
    return swapped


def main():
    global player_is_white
    post_player = requests.post(BASE + "board", {"option": "post_player", "nickname": nickname})
    get_player = requests.get(BASE + "board", {"option": "get_player", "nickname": nickname})
    player_is_white = get_player.json()
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    load_images()  # only do this once, before while loop
    sq_selected = ()  # No square is selected initially, keep track of last click of the user (tuple: row, col).
    player_clicks = []  # keep track of the player clicks, 2 tuples: [(6, 4), (4, 4)]
    running = True
    gameOver = False
    while running:
        game_running = requests.get(BASE + "board", {"option": "game_running?", "nickname": nickname})
        running = game_running.json()
        for e in p.event.get():
            if e.type == p.QUIT:
                reset_game = requests.post(BASE + "board", {"option": "reset"})
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                if not gameOver:
                    location = p.mouse.get_pos()  # (x, y) location of mouse
                    col = location[0] // SQ_SIZE
                    row = location[1] // SQ_SIZE
                    if sq_selected == (row, col):  # The user clicked the same square twice
                        sq_selected = ()  # Deselect
                        player_clicks = []  # Clear Player Clicks
                    else:
                        if player_is_white:
                            sq_selected = (row, col)
                            player_clicks.append(sq_selected)  # append for both 1st and 2nd clicks
                        else:
                            sq_selected = swap_clicks(row, col)
                            player_clicks.append(sq_selected)
                    if len(player_clicks) == 2:  # After 2nd click
                        move = requests.put(BASE + "board", {"first_click_x": player_clicks[0][0],
                                                             "first_click_y": player_clicks[0][1],
                                                             "second_click_x": player_clicks[1][0],
                                                             "second_click_y": player_clicks[1][1],
                                                             "nickname": nickname})
                        wasmoveMade = requests.get(BASE + "board", {"option": "wasMoveMade"})
                        moveMade = wasmoveMade.json()
                        sq_selected = ()  # Reset the user clicks
                        player_clicks = []
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:
                    undo = requests.post(BASE + "board", {"option": "undoMove"})
                elif e.key == p.K_r:
                    restart = requests.post(BASE + "board", {"option": "resetGame"})
                    sq_selected = ()
                    player_clicks = []
                    gameOver = False
        checkMate = requests.get(BASE + "board", {"option": "checkmate?"})
        staleMate = requests.get(BASE + "board", {"option": "stalemate?"})
        board = requests.get(BASE + "board", {"option": "board"})
        wasmoveMade = requests.get(BASE + "board", {"option": "wasMoveMade"})
        moveMade = wasmoveMade.json()

        whiteToMove = requests.get(BASE + "board", {"option": "whiteToMove"})
        if not player_is_white:
            board2 = []
            for i in reversed(board.json()):
                board2.append(list(reversed(i)))
            board_real = board2
        else:
            board_real = board.json()

        #isAnimate = requests.get(BASE + "board", {"option": "animate?"})
        #getAnimateInfo = requests.get(BASE + "board", {"option": "animate_info"})
        #if moveMade:
        #    animate = isAnimate.json()
        #    if animate:
        #        animateinfo = getAnimateInfo.json()
        #        print(animateinfo)
        #        if not player_is_white:
        #            startPos = swap_clicks(animateinfo["start_pos"][0], animateinfo["start_pos"][1])
        #            endPos = swap_clicks(animateinfo["end_pos"][1], animateinfo["end_pos"][1])
        #        else:
        #            startPos = animateinfo["start_pos"]
        #            endPos = animateinfo["end_pos"]
        #        animateMove(startPos, endPos, animateinfo["piece_moved"], animateinfo["piece_captured"], screen, board_real, clock)
        #    t.sleep(0.1)
        #    moveHasBeenMade = requests.post(BASE + "board", {"option": "moveHasBeenAnimated"})

        drawGameState(screen, board_real, sq_selected)

        if checkMate.json():
            gameOver = True
            if whiteToMove.json():
                drawText(screen, "Black wins by checkmate")
            else:
                drawText(screen, "White wins by checkmate")
        elif staleMate.json():
            gameOver = True
            drawText(screen, "Stalemate")

        clock.tick(MAX_FPS)
        p.display.flip()
        if game_running:
            if running:
                current_player = requests.get(BASE + "board", {"option": "current_player"})
                p.display.set_caption(f"Chess -- {current_player.json()}'s Turn -- {len(player_clicks)} click(s)")


def highlight_squares(screen, squares, player_is_white):
    if squares != []:
        startSquare = squares[0]
        squares.remove(squares[0])
        r, c = startSquare
        if not player_is_white:
            r, c = swap_clicks(r, c)
        s = p.Surface((SQ_SIZE, SQ_SIZE))
        s.set_alpha(100)  # transparency value
        s.fill(p.Color("blue"))
        screen.blit(s, (c * SQ_SIZE, r * SQ_SIZE))
        # highlight moves from square
        s.fill(p.Color("yellow"))
        for square in squares:
            r, c = square
            if not player_is_white:
                r, c = swap_clicks(r, c)
            screen.blit(s, (c * SQ_SIZE, r * SQ_SIZE))

def previous_move_highlighting(screen, squares, player_is_white):
    r, c = (squares[0][0], squares[0][1])
    if not player_is_white:
        r, c = swap_clicks(r, c)
    s = p.Surface((SQ_SIZE, SQ_SIZE))
    s.set_alpha(100)
    s.fill(p.Color("blue"))
    screen.blit(s, (c * SQ_SIZE, r * SQ_SIZE))
    r, c = (squares[1][0], squares[1][1])
    if not player_is_white:
        r, c = swap_clicks(r, c)
    s.fill(p.Color("yellow"))
    screen.blit(s, (c * SQ_SIZE, r * SQ_SIZE))

def drawGameState(screen, board, sq_selected):
    global player_is_white
    drawBoard(screen)  # draw squares on the board
    # add in piece highlighting or move suggestions (later)
    drawPieces(screen, board)  # draw pieces on top of those squares
    if sq_selected != ():
        highlighted_squares = requests.get(BASE + "board", {"option": "highlight_squares", "sq_selected_row": sq_selected[0], "sq_selected_col": sq_selected[1]})
        squares = highlighted_squares.json()
        highlight_squares(screen, squares, player_is_white)
    has_move_made = requests.get(BASE + "board", {"option": "has_move_made?"})
    moveMade = has_move_made.json()
    if moveMade:
        draw_last_move = requests.get(BASE + "board", {"option": "previous_move_highlight"})
        lastMove = draw_last_move.json()
        previous_move_highlighting(screen, lastMove, player_is_white)

def drawBoard(screen):
    global colours
    colours = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            colour = colours[((r+c) % 2)]
            p.draw.rect(screen, colour, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":  # not an empty square.
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


"""
Animating a move
"""


def animateMove(startPos, endPos, pieceMoved, pieceCaptured, screen, board, clock):
    global colours
    coords = []  # list of coords the animation will move through
    dR = endPos[0] - startPos[0]
    dC = endPos[1] - startPos[1]
    framesPerSquare = 5  # frames to move 1 square of the animation
    frameCount = (abs(dR) + abs(dC)) * framesPerSquare
    print(frameCount)
    for frame in range(frameCount + 1):
        r, c = (startPos[0] + dR*frame/frameCount, startPos[1] + dC*frame/frameCount)
        drawBoard(screen)
        drawPieces(screen, board)
        # erase the piece moved from its ending square
        colour = colours[(endPos[0] + endPos[1]) % 2]
        endSquare = p.Rect(endPos[1]*SQ_SIZE, endPos[0]*SQ_SIZE, SQ_SIZE, SQ_SIZE)
        p.draw.rect(screen, colour, endSquare)
        # draw captured piece onto rectangle
        if pieceCaptured != "--":
            screen.blit(IMAGES[pieceCaptured], endSquare)
        # draw moving pieces
        screen.blit(IMAGES[pieceMoved], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
        p.display.flip()
        clock.tick(60)


def drawText(screen, text):
    font = p.font.SysFont("Helvitca", 50, False, False)
    textObject = font.render(text, 0, p.Color("Black"))
    textLocation = p.Rect(0, 0, WIDTH, HEIGHT).move(WIDTH / 2 - textObject.get_width() / 2, HEIGHT / 2 - textObject.get_height() / 2)
    screen.blit(textObject, textLocation)
    textObject = font.render(text, 0, p.Color("Blue"))
    screen.blit(textObject, textLocation.move(2, 2))


if __name__ == "__main__":
    main()
