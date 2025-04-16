

def run_game(game_logic, description):
    """
    Общий движок для запуска игр
    :param game_logic: функция, содержащая логику конкретной игры
    :param description: описание игры для пользователя
    """
    print("Welcome to the Brain Games!")
    print(description)
    print("May I have your name?")
    name = input().strip()
    print(f"Hello, {name}!")
    
    while True:
        question, correct_answer = game_logic()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip()
        
        if str(user_answer) == str(correct_answer):
            print("Correct! Let's try again!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")