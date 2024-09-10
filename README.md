Project Shakes
--------------

Introduction
-------

Shakes is a Rock, Paper, Scissors implementation that allows for local players
to play the game locally (for now)

Project Components
-------

The components needed to play the game are:

* Redis server - holds game state
* Shakes API service - hosts the Rock, Paper , Scissors game API

Approach
-------

The approach that I have taken for Shakes is to implement the backend component
of the product along with an object storage component (REDIS). My reason for taking this route
is that I have more familiarity with the backend and its associated pieces and have a better
mental model of what is needed to provide a Rock, Paper, Scissors game service that could then
be used with a frontend that is able to present players with a user experience that is expertly
constructed. This also keeps me from flailing since I can get to work and incrementally build out
the web service.

My choice of REDIS is to allow for an object storage component that let's me take advantage of the
rich collection of storage types that are available to me in REDIS. This component can also be swapped
out at any time once the service is productionized.


Features Implemented
-------
- Added model for Rock, Paper, Scissors game choices
- Added model for game round history (wins, losses, players, etc..)
- Added endpoint for initializing a new game
- Added endpoint for saving an existing game
- Added endpoint for retrieving an existing game
- Added logic for CPU player

Getting Started
-------

In order to run the api and the example in the example directory , the following prerequisites are needed:
- redis
- redis-py
- python 3.12+
- poetry

From the root directory, create a new poetry shell:
`$ poetry shell`

Once you are in the shell, install all of the dependencies:
`$ poetry install`

Then , build and install the shakes package:
`$ bash build.sh`

Lastly, run the api in one terminal and then , open a new terminal and run the example:
`$ fastapi dev main.py`
`$ python examples/rounds.py`


TODO
-------
- Automated tests
- Simple summary stats for Games
- UI for players to play the game in a browser (single browser, against the CPU)
- UI enhancement for players to play the game in different browsers (CPU opponent optional)
- CI/CD for image creation
- CI/CD for pre-commit (pytest, pylint, vulture , deptry, etc..)
- CI/CD for pod deploy (helm chart with deploy to k8s)
