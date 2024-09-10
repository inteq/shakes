from pydantic import BaseModel

from typing import Optional

class Player(BaseModel):
    uuid: Optional[str|None] = None
    email: str
    username: str

class Scores(BaseModel):
    wins: Optional[int|None] = 0
    losses: Optional[int|None] = 0
    ties: Optional[int|None] = 0

class GRecord(BaseModel):
    firstchoice: str
    secondchoice: str
    winner: str

class Game(BaseModel):
    uuid: Optional[str|None] = None
    players: dict[str,Scores]
    history: list[GRecord]

class Shoot(BaseModel):
    playeruuid:str
    gameuuid: str
    choice:str
