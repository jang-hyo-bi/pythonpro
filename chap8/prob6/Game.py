import pickle
print("        Welcome to Trivia Challenge!             ")

def load_questions(file_name):
    questions = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        idx = 0
        while idx < len(lines):
            if lines[idx].startswith('question:'):
                question = lines[idx].split(': ')[1].strip()
                choices = lines[idx + 1].split(': ')[1].strip().split(';')
                answer = lines[idx + 2].split(': ')[1].strip()
                questions.append({'question': question, 'choices': choices, 'answer': answer})
                idx += 3
            else:
                idx += 1
    return questions

def display_question(question, choices):
    print(f"Question: {question}")
    for idx, choice in enumerate(choices, start=1):
        print(f"                     {idx} -  {choice}          ")

def trivia_game(questions):
    score = 0

    for idx, qna in enumerate(questions, start=1):
        question = qna['question']
        choices = qna['choices']
        answer = qna['answer']

        display_question(question, choices)

        user_choice = input("What's your answer?:  ").strip()

        try:
            user_choice = int(user_choice)
            user_answer = choices[user_choice - 1]
        except (ValueError, IndexError):
            user_answer = None

        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {answer}")

    print(f"\nGame Over!")

if __name__ == "__main__":
    file_name = 'questions.pickle'
    loaded_questions = load_questions(file_name)

    if loaded_questions:
        trivia_game(loaded_questions)
    else:
        print("Failed to load questions from file. Please check the file or its format.")
