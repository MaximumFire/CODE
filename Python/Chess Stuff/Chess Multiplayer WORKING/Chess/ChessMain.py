"""
This is our main driver file.
It will be responsible for handling user input and displaying the current GameState object.
"""

import pygame as p
import ChessEngine as ChessEngine
import time as t


WIDTH = HEIGHT = 512  # 400 would also work
DIMENSION = 8  # dimensions of a chess board are 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15  # for animations later on
IMAGES = {}

"""
Initialize a global dictionary of images. This will be called exactly once in the main.
"""


def load_images():
    pieces = ["wP", "wR", "wN", "wB", "wQ", "wK", "bP", "bR", "bN", "bB", "bQ", "bK"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
    # Note: we can access an image by saying IMAGES["wP"]


"""
The main driver for our code. This will handle user input and updating the graphics.
"""


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    valid_moves = gs.getValidMoves()
    moveMade = False  # flag variable for when a move is made
    animate = False  # flag variable for when we should animate a move
    load_images()  # only do this once, before while loop
    running = True
    sq_selected = ()  # No square is selected initially, keep track of last click of the user (tuple: row, col).
    player_clicks = []  # keep track of the player clicks, 2 tuples: [(6, 4), (4, 4)]
    gameOver = False
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
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
                        sq_selected = (row, col)
                        player_clicks.append(sq_selected)  # append for both 1st and 2nd clicks
                    if len(player_clicks) == 2:  # After 2nd click
                        move = ChessEngine.Move(player_clicks[0], player_clicks[1], gs.board)
                        move_string = move.getChessNotation()
                        for i in range(len(valid_moves)):
                            if move == valid_moves[i]:
                                gs.makeMove(valid_moves[i])
                                moveMade = True
                                animate = True
                                sq_selected = ()  # Reset the user clicks
                                player_clicks = []
                        if not moveMade:
                            player_clicks = [sq_selected]
            # key handlers
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:  # undo when z is pressed
                    gs.undoMove()
                    moveMade = True
                    animate = False
                    gameOver = False
                if e.key == p.K_r:  # reset the game when r is pressed
                    gs = ChessEngine.GameState()
                    valid_moves = gs.getValidMoves()
                    sq_selected = ()
                    player_clicks = []
                    moveMade = False
                    animate = False
                    gameOver = False

        if moveMade:
            if animate:
                animateMove(gs.moveLog[-1], screen, gs.board, clock)
            valid_moves = gs.getValidMoves()
            moveMade = False
            animate = False

        drawGameState(screen, gs, valid_moves, sq_selected)

        if gs.checkMate:
            gameOver = True
            if gs.whiteToMove:
                drawText(screen, "Black wins by checkmate")
            else:
                drawText(screen, "White wins by checkmate")
        elif gs.staleMate:
            gameOver = True
            drawText(screen, "Stalemate")

        clock.tick(MAX_FPS)
        p.display.flip()
        if gs.whiteToMove:
            p.display.set_caption("Chess -- White's Turn")
        elif not gs.whiteToMove:
            p.display.set_caption("Chess -- Black's Turn")


"""
Highlight the square selected and moves for piece selected
"""


def highlightSquares(screen, gs, valid_moves, sq_selected):
    if sq_selected != ():
        r, c = sq_selected
        if gs.board[r][c][0] == ("w" if gs.whiteToMove else "b"):  # sq_selected is a piece that can be moved
            # highlight selected square
            s = p.Surface((SQ_SIZE, SQ_SIZE))
            s.set_alpha(100)  # transparency value
            s.fill(p.Color("blue"))
            screen.blit(s, (c*SQ_SIZE, r*SQ_SIZE))
            # highlight moves from square
            s.fill(p.Color("yellow"))
            for move in valid_moves:
                if (move.startRow, move.startCol) == (r, c):
                    screen.blit(s, (SQ_SIZE*move.endCol, SQ_SIZE*move.endRow))
    if gs.moveLog != []:  # at least 1 move has been played
        move = gs.moveLog[-1]
        # highlight starting square
        r, c = (move.startRow, move.startCol)
        s = p.Surface((SQ_SIZE, SQ_SIZE))
        s.set_alpha(100)  # transparency value
        s.fill(p.Color("blue"))
        screen.blit(s, (c * SQ_SIZE, r * SQ_SIZE))
        # hightlight ending square
        r, c = (move.endRow, move.endCol)
        s.fill(p.Color("yellow"))
        screen.blit(s, (c * SQ_SIZE, r * SQ_SIZE))



"""
Responsible for all the graphics within a current game state.
"""


def drawGameState(screen, gs, valid_moves, sq_selected):
    drawBoard(screen)  # draw squares on the board
    # add in piece highlighting or move suggestions (later)
    drawPieces(screen, gs.board)  # draw pieces on top of those squares
    highlightSquares(screen, gs, valid_moves, sq_selected)


"""
Draw the squares on the board. The top left square is always light.
"""


def drawBoard(screen):
    global colours
    colours = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            colour = colours[((r+c) % 2)]
            p.draw.rect(screen, colour, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


"""
Draw the pieces on the board using the GameState.board
"""


def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":  # not an empty square.
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


"""
Animating a move
"""


def animateMove(move, screen, board, clock):
    global colours
    coords = []  # list of coords the animation will move through
    dR = move.endRow - move.startRow
    dC = move.endCol - move.startCol
    framesPerSquare = 5  # frames to move 1 square of the animation
    frameCount = (abs(dR) + abs(dC)) * framesPerSquare
    for frame in range(frameCount + 1):
        r, c = (move.startRow + dR*frame/frameCount, move.startCol + dC*frame/frameCount)
        drawBoard(screen)
        drawPieces(screen, board)
        # erase the piece moved from its ending square
        colour = colours[(move.endRow + move.endCol) % 2]
        endSquare = p.Rect(move.endCol*SQ_SIZE, move.endRow*SQ_SIZE, SQ_SIZE, SQ_SIZE)
        p.draw.rect(screen, colour, endSquare)
        # draw captured piece onto rectangle
        if move.pieceCaptured != "--":
            screen.blit(IMAGES[move.pieceCaptured], endSquare)
        # draw moving pieces
        screen.blit(IMAGES[move.pieceMoved], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
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
