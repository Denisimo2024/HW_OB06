import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона.")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        print("Игра началась!")
        while self.player.is_alive() and self.computer.is_alive():
            self.player_turn()
            if self.computer.is_alive():
                self.computer_turn()
        self.declare_winner()

    def player_turn(self):
        print(f"\nВаш ход! Здоровье: {self.player.health} | Здоровье противника: {self.computer.health}")
        self.player.attack(self.computer)
        if not self.computer.is_alive():
            print(f"{self.computer.name} погиб.")

    def computer_turn(self):
        print(f"\nХод компьютера! Здоровье: {self.computer.health} | Здоровье противника: {self.player.health}")
        self.computer.attack(self.player)
        if not self.player.is_alive():
            print(f"{self.player.name} погиб.")

    def declare_winner(self):
        if self.player.is_alive():
            print(f"\n{self.player.name} победил!")
        else:
            print(f"\n{self.computer.name} победил!")


# Основная часть игры
if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    player = Hero(player_name)
    computer = Hero(name="Компьютер", attack_power=random.randint(10, 30))

    game = Game(player, computer)
    game.start()