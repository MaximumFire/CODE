import random as r

pieceScore= {"K": 0, "Q": 10, "R": 5, "B": 3, "N": 3, "P": 1}
CHECKMATE = 1000
STALEMATE = 0


def findRandomMove(validMoves):
    i = r.randint(0, len(validMoves) - 1)
    return validMoves[i]


def findBestMove(gs, valid_moves):
    turnMultiplier = 1 if gs.whiteToMove else -1
    opponentMinMaxScore = CHECKMATE
    bestPlayerMove = None
    for playerMove in valid_moves:
        gs.makeMove(playerMove)
        opponentsMoves = gs.getValidMoves()
        opponentMaxScore = -turnMultiplier * CHECKMATE
        for opponentsMove in opponentsMoves:
            gs.makeMove(opponentsMove)
            if gs.checkMate:
                score = -CHECKMATE
            elif gs.staleMate:
                score = STALEMATE
            else:
                score = -turnMultiplier * scoreMaterial(gs.board)
            if score > opponentMaxScore:
                opponentMaxScore = score
            gs.undoMove()
        if opponentMinMaxScore > opponentMaxScore:
            opponentMinMaxScore = opponentMaxScore
            bestPlayerMove = playerMove
        gs.undoMove()
    return bestPlayerMove



"""
Score board based on material.
"""
def scoreMaterial(board):
    total = 0
    for row in board:
        for square in row:
            if square[0] == "w":
                total += pieceScore[square[1]]
            elif square[0] == "b":
                total -= pieceScore[square[1]]
    return total
