
game_uuid:<uuid>,



'int3q':{'uid':'<uuid>','email':'email@email.com'}

shakes:players:<uuid>
   base64 , gzip encoded json object 
      email
      player_name
shakes:players:cpu
  base64, gzip encoded json object
      email 
      player_name

shakes:games:<uuid>
  base64, gzip encoded json object
  player_count: 2,
  players:[
    "int3q": {'wins':10,'losses':2,'ties':10},
    "cpu" : {'wins':2,'losses':20,'ties':5},
  ],
  'history': [
    ["rock","scissors","int3q"],
    ["paper","paper","tie"],
    ["rock","paper","cpu"],
  ]

===============================================================
import base64
import gzip
import json
import uuid

In [13]: game_state
Out[13]:
{'uuid': '6cd70006-f430-42dd-bd07-1058c22207b2',
 'players': ['505e8929-cb18-43a4-b339-81026d5f82d4',
  '96f4b706-f214-4803-a54a-d57774c2bcc2'],
 'history': [['rock', 'papers', '505e8929-cb18-43a4-b339-81026d5f82d4']]}

In [15]: base64.b64encode(json.dumps(game_state).encode("utf8"))
Out[15]: b'eyJ1dWlkIjogIjZjZDcwMDA2LWY0MzAtNDJkZC1iZDA3LTEwNThjMjIyMDdiMiIsICJwbGF5ZXJzIjogWyI1MDVlODkyOS1jYjE4LTQzYTQtYjMzOS04MTAyNmQ1ZjgyZDQiLCAiOTZmNGI3MDYtZjIxNC00ODAzLWE1NGEtZDU3Nzc0YzJiY2MyIl0sICJoaXN0b3J5IjogW1sicm9jayIsICJwYXBlcnMiLCAiNTA1ZTg5MjktY2IxOC00M2E0LWIzMzktODEwMjZkNWY4MmQ0Il1dfQ=='

In [16]: gzip.zlib.compress(base64.b64encode(json.dumps(game_state).encode("utf8")))
Out[16]: b'x\x9c%\xce\xcdr\x83 \x14@\xe1W\x02\x7f\x16]dA\xc5f`\xbc0Lh\x15v\x89\xb6\x96\x8b6\x8b8c\xe0\xe9\xdb\xa4/\xf0\x9d\xf3\x99$\x9d\xfa%\n\xbc\xce\x02=z>\xee\xc0Y\xd1\xf5\x8e@f\x9b\xe22\xfa\x86\x06\xcfY\xd9\xd9vW\xf6\x1b\x01E\x02>\x05\x08\xe2&\x1a\xb9_\x8eo\xb5\x1fd~\x18}\x12\x14\xf8\xc7\xa2yL\xfaD\xd1a[u\xd6dg\xcd\xe6\x10\xb2>\x91\n,Kj5\xd4\xe3\x9c<7\xa1kX\xd0\xd6\xaf\xea(J\xe0n\xf3(\xee\xaa!Ds\x96\xbb\xbe\xa5\xea\xd8n\x9e\xbf\x97*\x8f\xc4e\x19\\\x01I,\xe4\xd1\xbe\x9e\x07E.\xa5\xac\x9fmz\x0b\xe3\xfa\x82\xe7\xf4\xff\xe5\x86\xd7e\xfc\x81\xa7\xaf,\xa3\xde\xce5`\xdc\\!\xee\xfa\xcf\x87\xa2%]/2\xe4\xb8i\xde\xee\x80>\xaa\xdeU\xb0\x1a"\x16:}\x99\xc3\xe1\x17a\xab_{'

===============================================================

In [16]: pprint.pprint(RULE_TABLE)
{'paper_paper': -1,
 'paper_rock': 0,
 'paper_scissors': 1,
 'rock_paper': 1,
 'rock_rock': -1,
 'rock_scissors': 0,
 'scissors_paper': 0,
 'scissors_rock': 1,
 'scissors_scissors': -1}

 {'choice': 'rock',
 'gameuuid': '8be4e135-e72b-40a6-91ea-dad1d45cf78d',
 'playeruuid': '7a78187c-3203-4cc9-9e3c-f9c58e6d56b6'}

In [17]: def play_game(player_1_choice,player_2_choice):
    ...:     return RULE_TABLE.get(f"{player_1_choice}_{player_2_choice}",-2)

================================================================

(Pdb) shoot_result
GRecord(firstchoice='rock', secondchoice='rock', winner='tie')
(Pdb) game_model
Game(uuid='8be4e135-e72b-40a6-91ea-dad1d45cf78d', players={'int3q': Scores(wins=0, losses=0, ties=0), 'cpu': Scores(wins=0, losses=0, ties=0)}, history=[])
(Pdb) game_model.players
{'int3q': Scores(wins=0, losses=0, ties=0), 'cpu': Scores(wins=0, losses=0, ties=0)}
(Pdb) game_model.history
[]
================================================================
player_data = {"username":"int3q","email":"justin.simms@gmail.com"}

resp = requests.post("http://0.0.0.0:8000/shakes/players/create/",data=json.dumps(player_data))

resp = requests.post("http://0.0.0.0:8000/shakes/games/create/7a78187c-3203-4cc9-9e3c-f9c58e6d56b6")

resp = requests.get("http://0.0.0.0:8000/shakes/players/list/")

resp = requests.post("http://0.0.0.0:8000/shakes/games/shoot/",data=json.dumps(shoot_model))



