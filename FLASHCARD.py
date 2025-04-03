""" import json
import random
try:
    with open("flashCard.json", "r") as file:
        words_data = json.load(file)
except FileNotFoundError:"""
words_data = []

class Teacher:
    def __init__(self, name):
        self.name = name
    def login(self):
        return f"you are logged in as {self.name}"
    def add_words(self):
        key = input("the word")
        keys= []
        value = input("the definition")
        values
        new_word = dict(zip(keys, values))
        words_data.append(new_word)  # Add the new word to the words_data

class Student:
    def __init__(self, name):
        self.name = name
    def login(self):
        return f"you are logged in as {self.name}"
"""     def quiz(self):
        quizzie() """

class Word:
    def __init__(self, word, definition):
        self.word = word
        self.definition = definition
    def to_dict(self):
        return {"word": self.word, "definition": self.definition}

""" words = [
    Word("Blah", "This word is blah"),
    Word("r", "r")
]      

word = Word("Chevrolet", "A very expensive car brand")
words_data.append(word) """

""" with open("flashCard.json", "w") as file:
    json.dump(words_data, file, indent=4) """

""" def quizzie(streak,points):
    question = random.randint()
    answer = input("enter the definition")
# random digit -> find the corresponding word    
    if definition == answer:
        points = points*streak*2
        streak +=1
    else:
        print("incorrect")
        streak = 0 """

Sofia = Student("Sofia")
print(Sofia.login())

