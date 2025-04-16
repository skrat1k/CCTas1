import random
from game_engine import run_game

def progression_game_logic():
    """Логика игры с геометрической прогрессией"""
    start = random.randint(1, 5)
    ratio = random.randint(2, 5)
    length = random.randint(5, 10)
    
    progression = [start * ratio**i for i in range(length)]
    hidden_pos = random.randint(0, length - 1)
    correct_answer = progression[hidden_pos]
    
    progression_display = progression.copy()
    progression_display[hidden_pos] = '..'
    question = ' '.join(map(str, progression_display))
    
    return question, correct_answer

def play_progression_game():
    """Запуск игры с прогрессией"""
    description = "What number is missing in the geometric progression?"
    run_game(progression_game_logic, description)

if __name__ == "__main__":
    play_progression_game()
