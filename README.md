# Kuhn Poker Server Backend

This repository contains the server-side implementation for the PokerBot group project. Your agent (client) can interact with the server for game coordination and administration. You can start this server locally to test your implementation.


## Setup

_Setup the Virtual Environment_

Open a new terminal in VSCode and create a new virtual environment by typing `conda env create -f environment.yml`. This command will create a `pokerbot39` virtual environment, if not already created by the client repository. For consistency, the client and server backend will use the same virtual environment. Activate the environment by `conda activate pokerbot39`.

_Generate the Game Protocol_

Generate the game protocol by typing `.\generate-proto.sh`. This will setup protocols for the agent to interact with a (local) game server.


_Start a Local Server_

You can now start a local server instance:

```bash
python manage.py runserver --settings=configurations.dev.settings
```

By default, the server will create two player tokens and print them at startup, e.g:
```bash
Test player token: 5e527757-0187-4511-a7dd-825fe2014d0a
Test player token: f9265243-b208-48b4-9cb9-7a865b6baaed
```
These tokens can be used for local clients to connect, see the `poker-server-client` readme.


## Custom Bot Players

The server backend allows your agent to play against a bot, but the implemented bot is not so clever - it is just an agent that plays random moves. To add a new bot create a subfolder in the `bots` directory with a clever agent implementation.


## Docker Desktop

You can also run a local server backend instance with Docker. If you have [Docker Desktop](https://www.docker.com/products/docker-desktop) installed on your machine, use the following command to start local server:

```bash
# First usage of this command is generally very slow. Subsequent usages will execute faster and will reuse cached docker image
docker-compose up
```

You may need to run `docker-compose up` twice for the first time to properly generate the server database layout.