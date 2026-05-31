# -*- coding: utf-8 -*-
class ScoreBoard:
    def __init__(self, player_wins, computer_wins):
        self.player_wins = player_wins
        self.computer_wins = computer_wins

    def update_score(self, result):
        if "Вы победили" in result:
            self.player_wins += 1
        elif 'Вы проиграли' in result:
            self.computer_wins += 1

    def display_score(self):
        return f"Победы игрока: {self.player_wins}, Победы компьютера: {self.computer_wins}"

    def save_score(self, score, filename='score.txt'):
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                for line in score:
                    file.write(line + '\n')
        except IOError as e:
            print(f'Ошибка при сохранении файла: {e}')

    def load_score(self, filename='score.txt', encoding='utf-8'):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return file.readlines()
        except FileNotFoundError:
            print('Файл не найден')
            return []