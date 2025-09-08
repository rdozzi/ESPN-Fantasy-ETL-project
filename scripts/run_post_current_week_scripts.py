"""Module to run scripts for the previous week after the ESPN cutoff"""

from etl.extract import (
    get_power_rankings,
    get_weekly_match_data_by_matchup,
    get_team_info_by_week,
)
from etl.transform import (
    transform_power_rankings,
    transform_weekly_match_results,
    transform_weekly_team_info,
)


def current_week_scripts():
    """function to extract and transform on power rankings, weekly match data, and team info"""

    get_power_rankings()
    power_rankings = transform_power_rankings()
    get_weekly_match_data_by_matchup()
    weekly_match_results = transform_weekly_match_results()
    get_team_info_by_week()
    weekly_team_info = transform_weekly_team_info()

    print(
        "power_rankings, match_results, team_info",
        power_rankings,
        weekly_match_results,
        weekly_team_info,
    )


if __name__ == "__main__":
    current_week_scripts()
