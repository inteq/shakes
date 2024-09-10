from fastapi import FastAPI
from pydantic import BaseModel

from shakes import models
from shakes import games
from shakes import players

description = """
    The Shakes API implements a rock,paper, scissors
    web service that allows a player to play RPS against
    a CPU opponent.
"""

app = FastAPI(
    title="Shakes API",
    description=description,
)

@app.get("/shakes/games/list/{player_uuid}")
async def list_games(player_uuid:str) -> list[models.Game]:
    return games.get_games(player_uuid)

@app.post("/shakes/games/create/{player_uuid}")
async def create_game(player_uuid:str) -> models.Game:
    return games.create_game(player_uuid)

@app.post("/shakes/games/shoot/")
async def perform_shoot(shoot:models.Shoot) -> models.Game:
    return games.perform_shoot(shoot)

@app.get("/shakes/games/retrieve/{game_uuid}")
async def get_game(game_uuid:str) -> models.Game:
    return games.get_game(game_uuid)

@app.get("/shakes/players/list/")
async def list_players() -> list[models.Player]:
    return players.get_players()

@app.post("/shakes/players/create/")
async def create_player(player_data: models.Player) -> models.Player:
    return players.create_player(player_data)

@app.get("/shakes/players/retrieve/{player_uuid}/")
async def get_player(player_uuid) -> models.Player:
    return players.get_player_by_uuid(player_uuid)
