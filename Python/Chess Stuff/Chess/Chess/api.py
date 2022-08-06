from flask import Flask
from flask_restful import Resource, Api, reqparse, abort
from ChessEngine import *

app = Flask("ChessAPI")
api = Api(app)

gs = GameState()
valid_moves = gs.getValidMoves()
nicknames = []

class Board(Resource):

    def get(self):
        # board = []
        # if player.lower() == "black":
        #     for row in gs.board[::-1]:
        #         board.append(row[::-1])
        # elif player.lower() == "white":
        #     board = gs.board
        # else:
        #     abort(400, message = f"{player} is not a valid player identifier.")
        return gs.board


class Moves(Resource):

    def get(self, option):
        pass

    def put(self, option):
        global gs, valid_moves

        if option == "makemove":
            parser = reqparse.RequestParser()
            parser.add_argument("startcol", location='args')
            parser.add_argument("startrow", location='args')
            parser.add_argument("endcol", location='args')
            parser.add_argument("endrow", location='args')

            args = parser.parse_args()

            valid_moves = gs.getValidMoves()
            start_square = (int(args["startrow"]), int(args["startcol"]))
            end_square = (int(args["endrow"]), int(args["endcol"]))

            move_made = False
            for move in valid_moves:
                if ((move.start_row, move.start_col) == start_square) and ((move.end_row, move.end_col) == end_square):
                    gs.makeMove(move)
                    move_made = True

            return {"move_made": move_made}

        elif option == "undomove":
            if len(gs.move_log) == 0:
                return {"move_undone": False}

            gs.undoMove()
            return {"move_undone": True}

        else:
            abort(404, message=f"{option} not a valid option.")



class Info(Resource):

    def get(self, option):

        if option == "game_over":
            return {"game_over": gs.checkmate or gs.stalemate}

        elif option == "white_to_move":
            return {"white_to_move": gs.white_to_move}

        elif option == "checkmate":
            return {"checkmate": gs.checkmate}

        elif option == "stalemate":
            return {"stalemate": gs.stalemate}

        else:
            abort(404, message=f"{option} not a valid option.")

    def put(self, option):

        if option == "nickname":

            parser = reqparse.RequestParser()
            parser.add_argument("nickname", location='args')

            args = parser.parse_args()

            nicknames.append(args["nickname"])

            if len(nicknames) == 1:
                return {"colour": "white"}
            else:
                return {"colour": "black"}

        else:
            abort(404, message=f"{option} not a valid option.")

    def post(self, option):

        if option == "close_game":

            parser = reqparse.RequestParser()
            parser.add_argument("nickname", location='args')

            args = parser.parse_args()

            nicknames.remove(args["nickname"])

        elif option == "reset_game":

            global gs

            gs = GameState()
            valid_moves = gs.getValidMoves()

        else:
            abort(404, message=f"{option} not a valid option.")


class Visuals(Resource):

    def get(self, option):

        if option == "animate":

            if len(gs.move_log) == 0:
                return {"message": "move log contains no moves"}

            gs.getValidMoves()

            return {"last_move": {"start_row": gs.move_log[-1].start_row,
                                  "start_col": gs.move_log[-1].start_col,
                                  "end_row": gs.move_log[-1].end_row,
                                  "end_col": gs.move_log[-1].end_col,
                                  "piece_captured": gs.move_log[-1].piece_captured,
                                  "is_enpassant": gs.move_log[-1].is_enpassant_move,
                                  "piece_moved": gs.move_log[-1].piece_moved},
                    "board": gs.board
                    }

        elif option == "highlight":
            valid_move_coords = []

            if len(gs.move_log) == 0:
                return {"message": "move log contains no moves"}

            gs.getValidMoves()

            for move in valid_moves:
                valid_move_coords.append([(move.start_row, move.start_col), (move.end_row, move.end_col)])

            return {"last_move": {"start_row": gs.move_log[-1].start_row,
                                  "start_col": gs.move_log[-1].start_col,
                                  "end_row": gs.move_log[-1].end_row,
                                  "end_col": gs.move_log[-1].end_col},
                    "white_to_move": gs.white_to_move,
                    "valid_move_coords": valid_move_coords,
                    "board": gs.board
                    }

        elif option == "movelog":

            if len(gs.move_log) == 0:
                return {"message": "move log contains no moves"}

            move_log = gs.move_log
            move_texts = []

            for i in range(0, len(move_log), 2):
                move_string = str(i // 2 + 1) + '. ' + str(move_log[i]) + " "
                if i + 1 < len(move_log):
                    move_string += str(move_log[i + 1]) + "  "
                move_texts.append(move_string)

            return move_texts

        else:
            abort(404, message=f"{option} not a valid option.")


api.add_resource(Board, "/board")
api.add_resource(Moves, "/moves/<option>")
api.add_resource(Info, "/info/<option>")
api.add_resource(Visuals, "/visuals/<option>")

if __name__ == "__main__":
    app.run(debug=True)