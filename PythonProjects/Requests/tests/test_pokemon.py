import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '87e7eaa9d1a5268815426e4d999c68f3'
HEADER = {'Content - Type' : 'application/json', 'trainer_token' : TOKEN} 
TRAINER_ID = '7104'

def test_status_code():
     response = requests.get(url= f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
     assert response.status_code == 200
    

    

