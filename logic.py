import requests
from random import randint

class Pokemon:
    pokemons = {}

    def __init__(self, trainer):
        self.pokemon_trainer = trainer
        self.number = randint(1, 1000)
        self.name = self.get_name()
        self.img = self.get_img()
        self.height = self.get_height()
        self.weight = self.get_weight()
        self.level = 1
        self.exp = 0
        self.hp = randint(1,50)
        self.power = randint(1,100)

        self.rare = self.weight > 300

        if self.rare:
            self.level += 1
            self.exp += 50

        Pokemon.pokemons[trainer] = self

    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.number}'
        response = requests.get(url)
        if response.status_code == 200:
            return requests.get(url).json()['forms'][0]['name']
        else:
            return "Pikachu"

    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.number}'
        response = requests.get(url)
        if response.status_code == 200:
            return requests.get(url).json()['sprites']['other']['official-artwork']['front_default']
        else:
            return "https://some-default.png"

    def get_height(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.number}'
        return requests.get(url).json().get('height', 4)

    def get_weight(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.number}'
        return requests.get(url).json().get('weight', 60)

    def info(self):
        rare_text = "🌟 Редкий покемон!" if self.rare else "Обычный покемон"
        return (f"Имя твоего покемона: {self.name}\n"
                f"Рост: {self.get_height() / 10} м\n"
                f"Вес: {self.get_weight() / 10} кг\n"
                f"{rare_text}\n"
                f"Уровень: {self.level}, Опыт: {self.exp}\n"               
                f"Сила: {self.power}\n"
                f"hp: {self.hp}")

    def show_img(self):
        return self.img
    
    def attack(self, enemy):
        if isinstance(enemy, Wizard): # Проверка на то, что enemy является типом данных Wizard (является экземпляром класса Волшебник)
            chance = randint(1,5)
            if chance == 1:
                return "Покемон-волшебник применил щит в сражении"


        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "
        

class Wizard(Pokemon):
    def info(self):
        return 'У тебя покемон-волшебник' + super().info()
    

class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(5,15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f"\nБоец применил супер-атаку силой:{super_power} "
    def info(self):
        return 'У тебя покемон-боец' + super().info()
    
if __name__ == '__main__':
    wizard = Wizard("username1")
    fighter = Fighter("username2")

    print(wizard.info())
    print()
    print(fighter.info())
    print()
    print(fighter.attack(wizard))