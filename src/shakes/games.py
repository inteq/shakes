import json
import redis
import uuid

from shakes import constants
from shakes import models
from shakes import utils
from shakes import players as game_players

def create_game(player_uuid:str) -> models.Game:

    redis_client = redis.Redis()

    # retrieve player data
    player_data = game_players.get_player_by_uuid(player_uuid)

    # retrieve cpu player data
    cpu_player_data = game_players.get_player("cpu")

    game_uuid = str(uuid.uuid4())

    # construct game data dict

    history = []

    players = {
        player_data.username:{'wins':0,'losses':0,'ties':0},
        cpu_player_data.username:{'wins':0,'losses':0,'ties':0},
    }

    game_data = {
        'uuid' : game_uuid,
        'players': players,
        'history': history
    }

    game_data_key = f"{constants.GAME_DATA_PREFIX}:player:{player_uuid}:game:{game_uuid}"

    # store game data by player and game uuids
    redis_client.set(game_data_key,json.dumps(game_data))

    game_lookup_key = f"{constants.GAME_UUID_PREFIX}:{game_uuid}"

    # store game creation entry by uuid (direct lookup) 
    redis_client.set(game_lookup_key,1)

    # return game object (dict)
    return models.Game(**game_data)

def get_game(game_uuid: str) -> models.Game:

    game_data_key = f"{constants.GAME_DATA_PREFIX}:player:*:game:{game_uuid}"

    redis_client = redis.Redis()

    game_keys = redis_client.keys(game_data_key)

    if not game_keys:
        return models.Game()

    game_uuid = game_keys[0]
    game_data = json.loads(redis_client.get(game_uuid.decode()))

    return models.Game(**game_data)

def get_games(player_uuid:str) -> list[models.Game]:

    game_collection = []

    game_data_glob = f"shakes:games:player:{player_uuid}:game:*"

    redis_client = redis.Redis()

    game_data_keys = redis_client.keys(game_data_glob)

    for game_data_key in game_data_keys:

        game_data = models.Game(**json.loads(redis_client.get(game_data_key.decode())))
        game_collection.append(game_data)

    return game_collection

def save_game_state(player_model:models.Player, game_model:models.Game) -> None:

    redis_client = redis.Redis()

    game_data_key = f"{constants.GAME_DATA_PREFIX}:player:{player_model.uuid}:game:{game_model.uuid}"

    # store game data by player and game uuids
    redis_client.set(game_data_key,json.dumps(game_model.dict()))

def perform_shoot(shoot:models.Shoot) -> models.Game:

    player_uuid = shoot.playeruuid
    player_model = game_players.get_player_by_uuid(player_uuid)
    game_uuid = shoot.gameuuid
    game_model = get_game(game_uuid)
    player_choice = shoot.choice
    cpu_choice = utils.random_shoot()
    shoot_result = utils.determine_result(player_model.username, player_choice,cpu_choice)

    game_model.history.append(shoot_result)

    if shoot_result.winner == "tie":
        game_model.players[player_model.username].ties += 1
        game_model.players["cpu"].ties += 1
    elif shoot_result.winner == player_model.username:
        game_model.players[player_model.username].wins += 1
        game_model.players["cpu"].losses += 1
    elif shoot_result.winner == "cpu":
        game_model.players[player_model.username].losses += 1
        game_model.players["cpu"].wins += 1

    save_game_state(player_model,game_model)

    return game_model

