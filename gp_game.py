import random

def geometric_progression_game():
    start = random.randint(1, 5)
    ratio = random.randint(2, 5)
    length = random.randint(5, 10)
    
    progression = [start * ratio**i for i in range(length)]
    
    hidden_pos = random.randint(0, length - 1)
    correct_answer = progression[hidden_pos]
    
    progression_display = progression.copy()
    progression_display[hidden_pos] = '..'
    progression_str = ' '.join(map(str, progression_display))
    
    print(f"Геометрическая прогрессия: {progression_str}")
    
    try:
        guess = int(input("Угадайте скрытое число: "))
    except ValueError:
        print("Пожалуйста, введите целое число.")
        return
    
    if guess == correct_answer:
        print("Правильно! Молодец!")
    else:
        print(f"Неправильно. Правильный ответ: {correct_answer}")
while True:
    geometric_progression_game()