"""Module to get data from espn_api and save to json"""

import os
import json

from dotenv import load_dotenv
from espn_api.football import League


load_dotenv()

year = 2025

league = League(
    league_id=int(os.getenv("LEAGUE_ID")),
    year=year,
    espn_s2=os.getenv("ESPN_S2"),
    swid=os.getenv("SWID"),
)

league.refresh()


def get_playoff_percentage():
    """Function to get the weekly playoff percentage. Executed in week 1"""

    teams = league.teams

    current_week = league.current_week

    weekly_playoff_percentage = []

    for team in teams:
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
        f"../data/raw/playoff_pct/weekly_playoff_percentage_by_team_week_{week}.json",
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(weekly_playoff_percentage, f, indent=2)


def get_power_rankings():
    """Function to get power_rankings. Executed in week 2"""

    week = league.current_week - 1

    power_rankings = league.power_rankings(week)

    with open(
        f"../data/raw/weekly_data/power_rankings_week_{week}.json",
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(power_rankings, f, indent=2)

    return power_rankings


def get_weekly_match_data_by_matchup():
    """Function to get the weekly box score by team. Executed in week 2"""
    league_year = league.year
    week = league.current_week - 1
    weekly_matchups = league.box_scores(week)

    weekly_match_results = {}
    weekly_match_results["week"] = week
    weekly_match_results["year"] = league_year

    for match in weekly_matchups:
        weekly_match_results["matchup_type"] = match.matchup_type

        home_team = match.home_team
        weekly_match_results[home_team]["score"] = match.home_score
        weekly_match_results[home_team]["is_home_team"] = True
        weekly_match_results[home_team]["opposing_team"] = match.away_team
        weekly_match_results[home_team]["projected"] = match.home_projected
        weekly_match_results[home_team]["lineup"] = match.home_lineup

        away_team = match.away_team
        weekly_match_results[away_team]["score"] = match.away_score
        weekly_match_results[away_team]["is_home_team"] = False
        weekly_match_results[away_team]["opposing_team"] = match.home_team
        weekly_match_results[away_team]["projected"] = match.away_projected
        weekly_match_results[away_team]["lineup"] = match.away_lineup

    with open(
        f"../data/raw/weekly_data/weekly_match_results_week_{week}.json",
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(weekly_match_results, f, indent=2)

    return weekly_match_results


def get_team_info_by_week():
    """Function to get team data. Executed in week 2"""

    week = league.current_week - 1
    teams = league.teams

    team_info_by_week = {}
    team_info_by_week["week"] = week

    for team in enumerate(teams):
        team_id = team.team_id
        team_name = team.team_name
        team_owner = team.owners[0]["firstName"] + " " + team.owners[0]["lastName"]
        team_wins = team.wins
        team_losses = team.losses
        team_ties = team.ties
        team_points_for = int(team.points_for)
        team_points_against = int(team.points_against)
        team_streak_type = team.streak_type
        team_streak_length = team.streak_length
        team_stats = team.stats
        team_standing = team.standing
        team_final_standing = team.final_standing

        team_info_by_week[team_name]["id"] = team_id
        team_info_by_week[team_name]["owner"] = team_owner
        team_info_by_week[team_name]["wins"] = team_wins
        team_info_by_week[team_name]["losses"] = team_losses
        team_info_by_week[team_name]["ties"] = team_ties
        team_info_by_week[team_name]["total_points_for"] = team_points_for
        team_info_by_week[team_name]["total_points_against"] = team_points_against
        team_info_by_week[team_name]["streak_type"] = team_streak_type
        team_info_by_week[team_name]["streak_length"] = team_streak_length
        team_info_by_week[team_name]["stats"] = team_stats
        team_info_by_week[team_name]["team_standing"] = team_standing
        team_info_by_week[team_name]["team_final_standing"] = team_final_standing

    with open(
        f"../data/raw/weekly_data/team_info_by_week_week_{week}.json",
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(team_info_by_week, f, indent=2)

    return team_info_by_week
