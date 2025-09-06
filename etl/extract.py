"""Module to get data from espn_api and save to json"""

import os


from dotenv import load_dotenv
from espn_api.football import League

load_dotenv()


def get_team_data():
    """Function to get the data from espn_api"""
    year = 2024

    league = League(
        league_id=int(os.getenv("LEAGUE_ID")),
        year=year,
        espn_s2=os.getenv("ESPN_S2"),
        swid=os.getenv("SWID"),
    )

    teams = league.teams

    # Stuff to load week to week
    # team name
    # owner name
    # team score
    # team number of wins
    # team number of losses
    # league power rankings
    # team playoff_pct
    # team streak_type
    # team streak_length


def save_data(data):
    """Function to save the incoming data"""
    return None
