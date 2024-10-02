# Kuhn Poker Server Backend

This repository contains the server-side implementation for the PokerBot group project. Your agent (client) can interact with the server for game coordination and administration. You can start this server locally to test your implementation.

## Setup

### Prerequisites

Docker Desktop installed on your machine

### Starting the Server

- Open a terminal in the project directory.
- Run the following command to start the local server:
```bash
docker-compose up
```
Note: The first time you run this command, it may take some time as Docker builds the image from scratch. Subsequent runs will be faster.
- You may need to run `docker-compose up` twice for the initial setup to properly generate the server database layout.

### Player Tokens

By default, the server will create some player tokens and print them at startup, e.g:

```bash
Test player token: 505ef7d7-22bb-47c2-25ba-bf044bbe9831
Test player token: ef084b69-ab77-4f0b-be4a-45deb4g93e3a
Test player token: 14858237-408e-4a20-958f-633f5fbe4708
Test player token: 69364161-68df-4445-84f8-b616f3ee4a84
```

These tokens can be used for local clients to connect. See the poker-server-client readme for more information on how to use these tokens.

### Configuration

You can inspect and modify parameters in the `./configurations/docker/settings.py` file. However, note that settings on the cloud server are hidden, and you will not know the exact values of those parameters (card image dimensions are fixed).

## Custom Bot Players

The server backend allows your agent to play against a bot on the server-side, but the implemented bot is not so clever - it is just an agent that plays random moves. To add a new bot create a subfolder in the `bots` directory with a clever agent implementation. This is not required for the assignment, but can be used for prototyping.
