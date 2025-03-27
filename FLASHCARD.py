import json

try:
    with open('your_file.json', 'r', encoding='utf-8-sig') as file:
        words_data = json.load(file)
except json.JSONDecodeError as e:
    print(f"Error reading JSON file: {e}")
    words_data = {}  # Initialize as an empty dictionary in case of failure
except FileNotFoundError:
    print("File not found.")
    words_data = {}  # Initialize as empty if file doesn't exist

# Now, you can proceed to work with words_data

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        return f"User: {self.name}, Email: {self.email}"
    
class teacher(User):
    def __init__(self, name, email, subject):
        super().__init__(name,email)
        self.subject = subject

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
new_word = Word("Chevrolet", "A very expensive car brand")
words.append(new_word.to_dict())

with open("flashCard.json", "w") as file:
    json.dump(words, file, indent=4)