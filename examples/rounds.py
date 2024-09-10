import json
import pdb
import pprint
import requests
import time

from shakes import utils

"""
This sample code creates a new user and game, then
runs through several rounds of Rock,Paper, Scissors using
the shakes api
"""

if __name__ == "__main__":

    # create a new player
    player_data = {"username":"int3q","email":"justin.simms@gmail.com"}
    resp = requests.post("http://0.0.0.0:8000/shakes/players/create/",data=json.dumps(player_data))
    # extracr the player uuid
    player_uuid = resp.json()["uuid"]
  
    # create a new RPS game
    resp = requests.post(f"http://0.0.0.0:8000/shakes/games/create/{player_uuid}")

    # retrieve the game uuid
    game_uuid = resp.json()["uuid"]

    # a shoot model is a representation of the player choosing Rock, Paper or Scissors and
    # that choice being passed to a game instance. 
    shoot_model = {"playeruuid":f"{player_uuid}","gameuuid":f"{game_uuid}","choice": utils.random_shoot()}

    # play a few roungs of RPS iusing the shakes API

    for i in range(20):

        resp = requests.post("http://0.0.0.0:8000/shakes/games/shoot/",data=json.dumps(shoot_model))
     
        # display the results of each round as a game model
        pprint.pprint(resp.json())

        time.sleep(1)
    
        shoot_model["choice"] = utils.random_shoot()
