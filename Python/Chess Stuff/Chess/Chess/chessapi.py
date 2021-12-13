from flask import Flask
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Api, Resource, reqparse, abort
import ChessEngine as ChessEngine

app = Flask(__name__)
api = Api(app)

gs = ChessEngine.GameState()

move_put_args = reqparse.RequestParser()
move_put_args.add_argument("first_click_x", type=int, help="first click x not defined", required=True)
move_put_args.add_argument("first_click_y", type=int, help="first click y not defined", required=True)
move_put_args.add_argument("second_click_x", type=int, help="second click x not defined", required=True)
move_put_args.add_argument("second_click_y", type=int, help="second click y not defined", required=True)
move_put_args.add_argument("nickname", type=str, help="nickname not sent")

move_post_args = reqparse.RequestParser()
move_post_args.add_argument("option", type=str, help="option not defined", required=True)
move_post_args.add_argument("nickname", type=str, help="nickname not sent")

board_get_args = reqparse.RequestParser()
board_get_args.add_argument("option", type=str, help="no option defined", required=True)
board_get_args.add_argument("nickname", type=str, help="nickname not sent")
board_get_args.add_argument("sq_selected_row", type=int, help="sq_selected_row not sent")
board_get_args.add_argument("sq_selected_col", type=int, help="sq_selected_col not sent")

valid_moves = gs.getValidMoves()
moveMade = False
players = []
player_colours = []
valid_move = False
animate = False


class Board(Resource):
    def get(self):
        global players, valid_move, animate
        args = board_get_args.parse_args()
        if args["option"] == "board":
            return gs.board
        elif args["option"] == "whiteToMove":
            return gs.whiteToMove
        elif args["option"] == "get_player":
            index = players.index(args["nickname"])
            if index == 0:
                return True
            else:
                return False
        elif args["option"] == "game_running?":
            if not (args["nickname"] in players):
                return False
            return True
        elif args["option"] == "valid_move?":
            return valid_move
        elif args["option"] == "current_player":
            if gs.whiteToMove:
                return players[0]
            else:
                return players[1]
        elif args["option"] == "checkmate?":
            return gs.checkMate
        elif args["option"] == "stalemate?":
            return gs.staleMate
        elif args["option"] == "wasMoveMade":
            return moveMade
        elif args["option"] == "moveLog":
            return gs.moveLog
        elif args["option"] == "highlight_squares":
            sq_selected = (args["sq_selected_row"], args["sq_selected_col"])
            squares = []
            if sq_selected != ():
                r, c = sq_selected
                print(r, c)
                if gs.board[r][c][0] == ("w" if gs.whiteToMove else "b"):  # sq_selected is a piece that can be moved
                    squares.append(sq_selected)
                    for move in valid_moves:
                        if (move.startRow, move.startCol) == (r, c):
                            squares.append((move.endRow, move.endCol))
            if squares == [sq_selected]:
                squares = []
            return squares
        elif args["option"] == "previous_move_highlight":
            if gs.moveLog != []:
                move = gs.moveLog[-1]
                startSquare = (move.startRow, move.startCol)
                endSquare = (move.endRow, move.endCol)
                return [startSquare, endSquare]
        elif args["option"] == "has_move_made?":
            if gs.moveLog != []:
                return True
            else:
                return False
        elif args["option"] == "animate_info":
            if gs.moveLog != []:
                return {"start_pos": (gs.moveLog[-1].startRow, gs.moveLog[-1].startCol),
                        "end_pos": (gs.moveLog[-1].endRow, gs.moveLog[-1].endCol),
                        "piece_captured": gs.moveLog[-1].pieceCaptured,
                        "piece_moved": gs.moveLog[-1].pieceMoved}
            else:
                return False
        elif args["option"] == "animate?":
            return animate

    def put(self):
        global valid_moves, moveMade, valid_move, animate
        valid_move = False
        valid_moves = gs.getValidMoves()
        args = move_put_args.parse_args()
        move = ChessEngine.Move((args["first_click_x"], args["first_click_y"]), (args["second_click_x"], args["second_click_y"]), gs.board)
        move_string = move.getChessNotation()
        for i in range(len(valid_moves)):
            if move == valid_moves[i]:
                valid_move = True
                if players.index(args["nickname"]) == 0:
                    if gs.board[args["first_click_x"]][args["first_click_y"]][0] == "w":
                        gs.makeMove(valid_moves[i])
                        moveMade = True
                        animate = True
                elif players.index(args["nickname"]) == 1:
                    if gs.board[args["first_click_x"]][args["first_click_y"]][0] == "b":
                        gs.makeMove(valid_moves[i])
                        moveMade = True
                        animate = True
        valid_moves = gs.getValidMoves()
        return move_string

    def post(self):
        global moveMade, players, player_colours, gs, valid_moves, animate
        args = move_post_args.parse_args()
        if args["option"] == "undoMove":
            gs.undoMove()
            moveMade = True
            animate = False
            valid_moves = gs.getValidMoves()
        elif args["option"] == "post_player":
            players.append(args["nickname"])
            if len(players) > 2:
                player_colours.append("w")
            else:
                player_colours.append("b")
        elif args["option"] == "reset":
            players = []
            player_colours = []
        elif args["option"] == "resetGame":
            gs = ChessEngine.GameState()
            valid_moves = gs.getValidMoves()
            moveMade = False
            animate = False
        elif args["option"] == "moveHasBeenAnimated":
            moveMade = False
            valid_moves = gs.getValidMoves()


api.add_resource(Board, "/board")

if __name__ == "__main__":
    app.run(debug=True)

