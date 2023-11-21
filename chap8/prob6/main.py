import pickle

questions = [
    {
        "question" : "In the story of Snow White, how many dwarfs are there?",
        "choices" :['seven', 'six', 'two', 'nine', 'one'],
        "answer" : "seven"
    },
    {
        "question" : "Which famous play features a character named Romeo?",
        "choices" : ['Romeo and Juliet', 'Romeo and chris', 'Romeo and chaly',' Romeo and hawn'],
        "answer" : "Romeo and Juliet"
    },
    {
        "question" : "What is the name of the largest ocean on Earth?",
        "choices" :['Pacific Ocean', 'Atlantic Ocean', 'west ocean', 'Indian Ocean'],
        "answer" : "Pacific Ocean"
    },
    {
        "question" : "How many colors are there in a rainbow?",
        "choices" : ['seven', 'eight', 'nine', 'ten' ],
        "answer" : "seven"
    }
]
with open('questions.pickle', 'w') as file:
    for item in questions:
        file.write(f"question: {item['question']}\n")
        choices_str = ';'.join(item['choices'])
        file.write(f"choices: {choices_str}\n")
        file.write(f"answer: {item['answer']}\n\n")
