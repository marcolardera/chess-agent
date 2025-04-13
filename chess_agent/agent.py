import requests
from google.adk.agents import Agent
from google.adk.tools import google_search, agent_tool

LICHESS_ENDPOINT = "https://lichess.org/api"
CHESSCOM_ENDPOINT = "https://api.chess.com"

MODEL = "gemini-2.0-flash"


def get_lichess_user(username: str) -> dict:
    """
    Get public user data of a Lichess account

    Args:
        username (str): Username of the Lichess account

    Returns:
        dict: user data
    """

    r = requests.get(f"{LICHESS_ENDPOINT}/user/{username}")
    resp = r.json()

    return resp


def get_chesscom_user(username: str) -> dict:
    """
    Get public user data of a Chess.com account

    Args:
        username (str): Username of the Chess.com account

    Returns:
        dict: user data including profile and statistics
    """

    r = requests.get(f"{CHESSCOM_ENDPOINT}/pub/player/{username}",
                     headers={
                         "User-Agent": "Chess agent"
                     })
    resp_profile = r.json()

    r = requests.get(f"{CHESSCOM_ENDPOINT}/pub/player/{username}/stats",
                     headers={
                         "User-Agent": "Chess agent"
                     })
    resp_stats = r.json()

    return {
        "profile": resp_profile,
        "stats": resp_stats
    }

web_search_agent = Agent(
    name="web_search_agent",
    model=MODEL,
    description="Web browsing agent",
    instruction="I'm an expert at searching informations on the web",
    tools=[google_search]
)
    
root_agent = Agent(
    name="chess_agent",
    model=MODEL,
    description="Agent to answer chess related questions",
    instruction="I'm an expert at answering chess related questions and extracting player data from Lichess and Chess.com",
    tools=[get_lichess_user, get_chesscom_user, agent_tool.AgentTool(agent=web_search_agent)]
)


