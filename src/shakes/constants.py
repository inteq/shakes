GAME_DATA_PREFIX = "shakes:games"
GAME_UUID_PREFIX = "shakes:games:created"
PLAYER_DATA_PREFIX = "shakes:players"
PLAYER_DATA_GLOB = f"{PLAYER_DATA_PREFIX}:*"
PLAYER_UUID_PREFIX = "shakes:lookups"
CPU_PLAYER_DATA_KEY = f"{PLAYER_DATA_PREFIX}:cpu"

ACCEPTABLE_CHOICES = [
    "rock",
    "paper",
    "scissors",
]

RULE_TABLE = {
 'paper_paper': -1,
 'paper_rock': 0,
 'paper_scissors': 1,
 'rock_paper': 1,
 'rock_rock': -1,
 'rock_scissors': 0,
 'scissors_paper': 0,
 'scissors_rock': 1,
 'scissors_scissors': -1
}
