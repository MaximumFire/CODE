from flask import Flask
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Api, Resource, reqparse, abort
import ChessEngine as ChessEngine

app = Flask(__name__)
api = Api(app)

gs = ChessEngine.GameState()

board_post_args = reqparse.RequestParser()
board_post_args.add_argument("player", type=str, help="Send player value (w/b)")


class Board:
    def get(self):
        pass

    def post(self):
        args = board_post_args.parse_args()



api.add_resource(Board, "/board")

if __name__ == "__main__":
    app.run(debug=True)

