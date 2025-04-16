def run_game(game_logic, description):
    """
    Общий движок для запуска игр
    :param game_logic: функция, содержащая логику конкретной игры
    :param description: описание игры для пользователя
    """
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ").strip()
    print(f"Hello, {name}!")
    print(description)
    
    correct_answers_needed = 3
    correct_answers = 0
    
    while correct_answers < correct_answers_needed:
        question, correct_answer = game_logic()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip()
        
        if str(user_answer) == str(correct_answer):
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")
