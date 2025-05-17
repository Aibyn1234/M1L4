from random import randint
import requests

class Pokemon:
    pokemons = {}

    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = randint(1, 1000)
        Pokemon.pokemons[pokemon_trainer] = self

    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['forms'][0]['name']
        else:
            return "Pikachu"

    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['sprites']['other']['official-artwork']['front_default']
        else:
            return "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/1.png"

    def get_height(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['height']
        else:
            return 4

    def get_weight(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['weight']
        else:
            return 60

    def info(self):
        return (f"Имя твоего покемона: {self.get_name()}\n"
                f"Рост: {self.get_height() / 10} м\n"
                f"Вес: {self.get_weight() / 10} кг")

    def show_img(self):
        return self.get_img()
