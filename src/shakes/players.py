import json
import redis
import uuid

from shakes import constants
from shakes import models
from shakes import utils

def create_player(player_data: models.Player) -> models.Player:

    player_data_key = f"{constants.PLAYER_DATA_PREFIX}:{player_data.username}"

    redis_client = redis.Redis()

    #HACK: to allow for a cpu 'player', check for its existence
    # and create one if it does not exist

    if not redis_client.exists(constants.CPU_PLAYER_DATA_KEY):

        utils.create_cpu_player(constants.CPU_PLAYER_DATA_KEY)

    if redis_client.exists(player_data_key):
        return get_player(player_data.username)

    user_uuid = str(uuid.uuid4())

    # construct user data dict

    user_data = {
        'uuid' : user_uuid,
        'username' : player_data.username,
        'email': player_data.email
    }

    # store user data by username
    redis_client.set(player_data_key,json.dumps(user_data))

    # add lookup key to retrieve user data by uuid
    player_lookup_key = f"{constants.PLAYER_UUID_PREFIX}:{user_uuid}"
    redis_client.set(player_lookup_key,player_data.username)

    # return uuid and user object (dict)
    return models.Player(**user_data)

def get_player(playername: str) -> models.Player:

    player_data_key = f"{constants.PLAYER_DATA_PREFIX}:{playername}"

    redis_client = redis.Redis()

    user_data = json.loads(redis_client.get(player_data_key))

    return models.Player(**user_data)

def get_player_by_uuid(player_uuid:str) -> models.Player:

    player_lookup_key = f"{constants.PLAYER_UUID_PREFIX}:{player_uuid}"

    redis_client = redis.Redis()

    player_name = redis_client.get(player_lookup_key)

    player_data_key = f"{constants.PLAYER_DATA_PREFIX}:{player_name.decode()}"

    user_data = json.loads(redis_client.get(player_data_key))

    return models.Player(**user_data)

def get_players() -> list[models.Player]:

    player_collection = []

    player_data_glob = f"{constants.PLAYER_DATA_GLOB}"

    redis_client = redis.Redis()

    user_data_keys = redis_client.keys(player_data_glob)

    for user_data_key in user_data_keys:

        player_data = models.Player(**json.loads(redis_client.get(user_data_key.decode())))
        player_collection.append(player_data)

    return player_collection
