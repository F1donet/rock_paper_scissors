import csv

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

    def save_to_file(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Игрок', 'Компьютер', 'Результат'])
            writer.writerow([self.player_wins, self.computer_wins, 'Сохранено'])
