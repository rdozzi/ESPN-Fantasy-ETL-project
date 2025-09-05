import os
import httpx
from dotenv import load_dotenv
from espn_api.football import League

load_dotenv()


league = League(
    league_id=os.getenv("LEAGUE_ID"),
    year=os.getenv("YEAR"),
    espn_s2=os.getenv("ESPN_S2"),
    swid=os.getenv("SWID"),
)
