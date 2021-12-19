from flask import Flask
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Api, Resource, reqparse, abort
import Engine as Engine

app = Flask(__name__)
api = Api(app)

# Global variables
gs = Engine.GameState()
games = []


class Game:
    def __init__(self, identifier: int, p1, p2, playercount: int, gamestate: Engine.GameState):
        self.id = identifier
        self.p1 = p1
        self.p2 = p2
        self.playercount = playercount
        self.gs = gamestate


class Player:
    def __init__(self, nickname: str, won: bool, isWhite: bool, isTurn: bool):
        self.isTurn = isTurn
        self.isWhite = isWhite
        self.won = won
        self.nickname = nickname


board_get_args = reqparse.RequestParser()
board_get_args.add_argument("id", type=int, help="id not sent", required=True)


class Board(Resource):
    def get(self):
        args = board_get_args.parse_args()
        requested_game = None
        for game in games:
            if game.id == args["id"]:
                requested_game = game
        return requested_game.gs.board

    def post(self):
        pass


setup_post_args = reqparse.RequestParser()
setup_post_args.add_argument("nickname", type=str, help="nickname not sent", required=True)
setup_post_args.add_argument("id", type=int, help="id not sent", required=True)


class Setup(Resource):
    def get(self):
        global games
        # Loop though created games to find a free spot
        for game in games:
            if game.playercount < 2:  # if free spot found
                game.playercount += 1  # take free spot
                return game.id  # return id to user
        # If no free spots found in games
        try:  # try to find previous game's id
            starting_id = games[len(games)-1].id
        except IndexError:  # if no games yet, set previous id to be 0
            starting_id = 0
        # create game with blank info and id
        games.append(Game(identifier=(starting_id+1), p1=Player("", False, False, False), p2=Player("", False, False, False), playercount=1, gamestate=Engine.GameState()))
        # return id to user
        return games[len(games)-1].id

    def post(self):
        args = setup_post_args.parse_args()
        nickname = args["nickname"]
        identifier = args["id"]
        for game in games:
            if game.id == identifier:
                if game.p1.nickname == "":
                    game.p1.nickname = nickname
                else:
                    game.p2.nickname = nickname


gameinfo_get_args = reqparse.RequestParser()
gameinfo_get_args.add_argument("id", type=int, help="id not sent", required=True)


class GameInfo(Resource):
    def get(self):
        args = gameinfo_get_args.parse_args()
        ls = []
        for game in games:
            if game.id == args["id"]:
                ls = [game.p1.nickname, game.p2.nickname]
        return ls

    def post(self):
        pass


api.add_resource(Board, "/board")
api.add_resource(Setup, "/setup")
api.add_resource(GameInfo, "/gameinfo")

if __name__ == "__main__":
    app.run(debug=True)
