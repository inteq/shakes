import json
import random
import redis
import uuid

from shakes import constants
from shakes import models

def create_cpu_player(player_data_key) -> None:

    redis_client = redis.Redis()

    user_uuid = str(uuid.uuid4())

    # construct user data dict

    user_data = {
        'uuid' : user_uuid,
        'username' : "cpu",
        'email': "cpu-no-email@nonexistent.com"
    }

    # store user data by username
    redis_client.set(player_data_key,json.dumps(user_data))

    # add lookup key to retrieve user data by uuid
    player_lookup_key = f"{constants.PLAYER_UUID_PREFIX}:{user_uuid}"
    redis_client.set(player_lookup_key,"cpu")

def determine_result(player_name:str, choice_one:str, choice_two:str) -> models.GRecord:

    winner = constants.RULE_TABLE.get(f"{choice_one}_{choice_two}",-2)

    if winner == 0:
        winner_label = player_name
    elif winner == 1:
        winner_label = "cpu"
    else:
        winner_label = "tie"
    
    game_round_result = models.GRecord(firstchoice=choice_one,secondchoice=choice_two,winner=winner_label)

    return game_round_result

def random_shoot() -> str:
    random.seed()
    return random.choice(constants.ACCEPTABLE_CHOICES)
