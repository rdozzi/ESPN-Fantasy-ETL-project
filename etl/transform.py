"""Module to transform incoming data"""

import os
import json

from dotenv import load_dotenv
from espn_api.football import League
import pandas as pd

load_dotenv()

YEAR = 2025

league = League(
    league_id=int(os.getenv("LEAGUE_ID")),
    year=YEAR,
    espn_s2=os.getenv("ESPN_S2"),
    swid=os.getenv("SWID"),
)

league.refresh()


def transform_playoff_percentage():
    """transform playoff_percentag into dataframe"""
    week = league.current_week
    with open(
        f"../data/raw/playoff_pct/weekly_playoff_percentage_by_team_week_{week}.json",
        encoding="utf-8",
    ) as f:
        raw = json.load(f)

    df = pd.DataFrame(raw)
    df["week"] = week

    output_file = f"../data/processed/playoff_pct/weekly_playoff_percentage_by_team_week_{week}.csv"
    df.to_csv(output_file, index=False)

    return df


def transform_power_rankings():
    """transform raw power rankings into dataframe"""
    week = league.current_week - 1
    with open(
        f"../data/raw/weekly_data/power_rankings_week_{week}.json", encoding="utf-8"
    ) as f:
        raw = json.load(f)

    power_ranking_unpacked = [
        {"rank": rank, "team_name": team.team_name} for rank, team in raw
    ]

    df = pd.DataFrame(power_ranking_unpacked)
    df["week"] = week

    output_file = f"../data/processed/power_rankings/power_rankings_week_{week}.csv"
    df.to_csv(output_file, index=False)

    return df


def transform_weekly_match_results():
    """transform weekly match results"""
    week = league.current_week - 1
    with open(
        f"../data/raw/weekly_data/weekly_match_results_week_{week}.json",
        encoding="utf-8",
    ) as f:
        raw = json.load(f)

    df = pd.DataFrame.from_dict(raw, orient="index").reset_index()
    df = df.rename(columns={"index": "team_name"})
    df["week"] = week

    output_file = (
        f"../data/processed/weekly_match_data/weekly_match_results_week_{week}.csv"
    )
    df.to_csv(output_file, index=False)

    return df


def transform_weekly_team_info():
    """transform weekly team_info"""
    week = league.current_week - 1
    with open(
        f"../data/raw/weekly_data/team_info_by_week_week_{week}.json",
        encoding="utf-8",
    ) as f:
        raw = json.load(f)

    df = pd.DataFrame.from_dict(raw, orient="index").reset_index()
    df = df.rename(columns={"index": "team_name"})
    df["week"] = week

    output_file = (
        f"../data/processed/weekly_team_info/team_info_by_week_week_{week}.csv"
    )
    df.to_csv(output_file, index=False)

    return df
