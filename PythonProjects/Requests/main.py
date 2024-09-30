import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '87e7eaa9d1a5268815426e4d999c68f3'
HEADER = {'Content - Type' : 'application/json', 'trainer_token' : TOKEN} 
body_pokemons = {
    "pokemon_id": "73621",
    "name": "бильбо",
    "photo_id": 2
}


'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemons)
print(response_create)'''



'''response_create = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemons)
print(response_create)'''

response_create = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokemons)
print(response_create)


