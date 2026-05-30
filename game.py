import random

def random_choice():
    return random.choice(["камень", "ножницы", "бумага"])

def check_winner(player1, player2):

    if player1 == "камень" and player2 == "ножницы":
        return "Вы победили. Камень побеждает ножницы"
    elif player1 == "ножницы" and player2 == "камень":
        return "Вы проиграли. Камень побеждает ножницы"
    elif player1 == "ножницы" and player2 == "бумага":
        return "Вы победили. Ножницы побеждают бумагу"
    elif player1 == "бумага" and player2 == "ножницы":
        return "Вы проиграли. Ножницы побеждают бумагу"
    elif player1 == "бумага" and player2 == "камень":
        return "Вы победили. Бумага побеждает камень"
    elif player1 == "камень" and player2 == "бумага":
        return "Вы проиграли. Бумага побеждает камень"
    else:
        return "Ничья"

while True:
    player1 = input("Введите ваш выбор (камень, ножницы, бумага): ").lower()
    if player1 != "камень" and player1 != "ножницы" and player1 != "бумага":
        continue
    player2 = random_choice()
    result = check_winner(player1, player2)
    print(f"Ваш выбор: {player1}")
    print(f"Компьютер выбрал: {player2}")
    print(f"Результат: {result}")
    if result == "Ничья":
        print("Играем ещё раз!")
    else:
        print("Спасибо за игру!")
        a = input("Сыграем еще раз?(да/нет): ").lower()
        if a == "нет":
            break
        else:
            continue
