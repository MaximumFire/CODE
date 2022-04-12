import ChessEngine as ChessEngine
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

gs = ChessEngine.GameState()
valid_moves = None
move_made = False
animate = False


class Board(Resource):
    def get(self):
        global gs
        return gs.board


class Move(Resource):
    def post(self, player_is_white, startrow, startcol, endrow, endcol):
        global gs, valid_moves, animate, move_made
        player_is_white = True if player_is_white == 1 else False
        if (player_is_white and gs.white_to_move) or (not player_is_white and not gs.white_to_move):
            move = ChessEngine.Move((startrow, startcol), (endrow, endcol), gs.board)
            valid_moves = gs.getValidMoves()
            for i in range(len(valid_moves)):
                if valid_moves[i] == move:
                    gs.makeMove(move)
                    return {"move_made": True}
        return {"move_made": False}


api.add_resource(Board, "/board")
api.add_resource(Move, "/move/<int:player_is_white>/<int:startrow>/<int:startcol>/<int:endrow>/<int:endcol>")
api.add_resource(Vars, "/vars/<string:option>")

if __name__ == "__main__":
    app.run(debug=True)


