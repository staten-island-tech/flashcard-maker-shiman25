import json
try:
    with open("flashCard.json", "r") as file:
        words_data = json.load(file)
except FileNotFoundError:
    words_data = []

class Teacher:
    def __init__(self, name):
        self.name = name
    def login(self):
        return f"you are logged in as {self.name}"
    def add_words(self):
        w = input("the word")
        d = input("the definition")
        new_word = Word(w, d)
        words_data.append(new_word.to_dict())  # Add the new word to the words_data lis
        

class Word:
    def __init__(self, word, definition):
        self.word = word
        self.definition = definition
    def to_dict(self):
        return {"word": self.word, "definition": self.definition}

words = [
    Word("Blah", "This word is blah"),
    Word("r", "r")
]      
word = Word("Chevrolet", "A very expensive car brand")
words_data.append(word.to_dict())

with open("flashCard.json", "w") as file:
    json.dump(words_data, file, indent=4)

""""""