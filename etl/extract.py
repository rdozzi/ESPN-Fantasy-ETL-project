"""Module to get data from espn_api and save to json"""

import os
import json
from pathlib import Path

from dotenv import load_dotenv
from espn_api.football import League
import pandas as pd


load_dotenv()


def get_playoff_percentage():
    """Function to get the weekly playoff percentage"""
    year = 2025

    league = League(
        league_id=int(os.getenv("LEAGUE_ID")),
        year=year,
        espn_s2=os.getenv("ESPN_S2"),
        swid=os.getenv("SWID"),
    )

    league.refresh()

    teams = league.teams

    current_week = league.current_week

    weekly_playoff_percentage = []

    for team in enumerate(teams):
        team_id = team.team_id
        team_name = team.team_name
        week = current_week
        team_playoff_perc = team.playoff_pct

        playoff_pct_data_per_week = {
            "id": team_id,
            "name": team_name,
            "week": week,
            "playoff_percentage": team_playoff_perc,
        }

        weekly_playoff_percentage.append(playoff_pct_data_per_week)

    with open(
        f"../data/raw/playoff_percentage_by_team_week_{week}", "w", encoding="utf-8"
    ) as f:
        json.dump(weekly_playoff_percentage, f, indent=2)


def get_team_data():
    """Function to get the data from espn_api"""
    year = 2025

    league = League(
        league_id=int(os.getenv("LEAGUE_ID")),
        year=year,
        espn_s2=os.getenv("ESPN_S2"),
        swid=os.getenv("SWID"),
    )

    league.refresh()

    # Stuff to load week to week
    # league power rankings
    # team name
    # team id
    # owner name
    # team score
    # team number of wins
    # team number of losses
    # team playoff_pct
    # team streak_type
    # team streak_length

    # ESPN resets its week at 12AM PST on Monday. To get last week's data, call current_week and subtract 1.
    current_week = league.current_week

    power_rankings = league.power_rankings(current_week - 1)

    teams = league.teams


def save_data(data):
    """Function to save the incoming data"""
    return None
