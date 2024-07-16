# Kuhn Poker Server Backend

This repository contains the server-side implementation for the PokerBot group project. Your agent (client) can interact with the server for game coordination and administration. You can start this server locally to test your implementation.


## Setup

_Setup the Virtual Environment_

Open a new terminal in VSCode and create a new virtual environment by typing `conda env create -f environment.yml` (non-windows users should use the corresponding environment file). This command will create a `pokerbot39` virtual environment, if it was not already created when setting up the client repository. For consistency, the client and server backend will use the same virtual environment. Activate the environment by `conda activate pokerbot39`.

_Install the Django web framework_

Django is a webdevelopment framework for Python, and needs to be installed using pip. All requirements for Django are listed in `requirements.txt` (and the corresponding environment file for non-windows users). With the `pokerbot39` environment active, install the Django requirements by typing
```bash
pip install -r requirements.txt
```

_Initialize the Game Protocol and the Database_

To generate the game protocol and the proper database layout simply run `python init.py`.

_Start a Local Server_

You can now start a local server instance:

```bash
python manage.py runserver --settings=configurations.dev.settings
```

By default, the server will create some player tokens and print them at startup, e.g:
```bash
Test player token: 505ef7d7-22bb-47c2-25ba-bf044bbe9831
Test player token: ef084b69-ab77-4f0b-be4a-45deb4g93e3a
Test player token: 14858237-408e-4a20-958f-633f5fbe4708
Test player token: 69364161-68df-4445-84f8-b616f3ee4a84
```
These tokens can be used for local clients to connect, see the `poker-server-client` readme. When running the backend for the first time, you may need to start the backend twice before the player tokens are generated.

You are free to inspect and modify parameters from the `./configurations/dev/settings.py` file. 
Note, however, that settings on the cloud server are hidden from you, and you will not know the exact values of those parameters (card image dimensions are fixed).


## Custom Bot Players

The server backend allows your agent to play against a bot on the server-side, but the implemented bot is not so clever - it is just an agent that plays random moves. To add a new bot create a subfolder in the `bots` directory with a clever agent implementation. This is not required for the assignment, but can be used for prototyping.


## Docker Desktop

You can also run a local server backend instance with Docker. If you have [Docker Desktop](https://www.docker.com/products/docker-desktop) installed on your machine, use the following command to start local server:

```bash
docker-compose up
```

Note that first usage of this command is generally very slow as it requires to build a Docker image from scratch. Subsequent usages should reuse the cached docker image and will execute faster. You will need to run `docker-compose up` twice for the initial setup to properly generate the server database layout.
