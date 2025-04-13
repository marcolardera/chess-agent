# chess-agent

Little chess informations agent for experimenting with Google ADK (https://github.com/google/adk-python).

It uses the following tools:

- get_lichess_user: custom function, calls the Lichess API for users data
- get_chesscom_user: custom function, calls the Chess.com API for users data
- google_search: built-in tool for web searching


## Setup & run

Pre-requirements: Python >= 3.10, uv (recommended)

Clone the repo, then create a .env file in the `chess_agent` folder:

```
GOOGLE_GENAI_USE_VERTEXAI="False"
GOOGLE_API_KEY="<YOUR API KEY>"
```

Create & sync the environment:

```
uv venv
source .venv/bin/activate
uv sync
```

(Without uv create a venv in the traditional way and then `pip install .`)

Run the agent in the web interface:

`àdk web`

Run the agent in the CLI:

`adk run chess_agent`

Serve the agent as a REST API:

`adk api_server`

