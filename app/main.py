import logging
import requests
from fastapi import FastAPI

app = FastAPI()
curryware_yahoo_api_controller_url = 'http://curryware-yahoo-api:8087/YahooApi'

FORMAT = ('%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] - '
              '%(message)s')
logging.basicConfig(format=FORMAT)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/v1/load_players')
async def load_players(league_id: str, team_id: str):
    load_player_endpoint = '/GetAllPlayers'
    request_url = curryware_yahoo_api_controller_url + load_player_endpoint
    response = requests.get(request_url, timeout=300)
    logger.info(f'Loading players for league {league_id} and team {team_id}')

    return response.content