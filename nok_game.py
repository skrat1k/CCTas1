import random
from game_engine import run_game

def calculate_nok(a, b, c):
    """Вычисление наименьшего общего кратного для трех чисел"""
    max_num = max(a, b, c)
    while True:
        if max_num % a == 0 and max_num % b == 0 and max_num % c == 0:
            return max_num
        max_num += 1

def nok_game_logic():
    """Логика игры с поиском НОК"""
    a, b, c = random.randint(1, 40), random.randint(1, 40), random.randint(1, 40)
    question = f"{a}, {b}, {c}"
    correct_answer = calculate_nok(a, b, c)
    return question, correct_answer

def play_nok_game():
    """Запуск игры с НОК"""
    description = "Find the smallest common multiple of given numbers."
    run_game(nok_game_logic, description)

if __name__ == "__main__":
    play_nok_game()

    