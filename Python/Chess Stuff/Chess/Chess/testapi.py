from flask import Flask
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Api, Resource, reqparse, abort
import ChessEngine as ChessEngine

app = Flask(__name__)
api = Api(app)

gs = ChessEngine.GameState()

get_args = reqparse.RequestParser()
get_args.add_argument("option", type=str, help="no option defined")

class Board(Resource):
    def get(self):
        args = get_args.parse_args()
        if args["option"] == "board":
            return gs.board
        else:
            return "hello"

api.add_resource(Board, "/board")

if __name__ == "__main__":
    app.run(debug=True)