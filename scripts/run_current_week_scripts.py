"""Module to define and run scripts from the current week"""

from etl.extract import get_playoff_percentage
from etl.transform import transform_playoff_percentage


def current_week_scripts():
    """function to execute extract and transform on weekly playoff percentage"""
    get_playoff_percentage()
    playoff_percentage = transform_playoff_percentage()

    print("Transformed Playoff Data:", playoff_percentage)


if __name__ == "__main__":
    current_week_scripts()
