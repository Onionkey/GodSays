import requests
import random
import textwrap
import os
import unicodedata

# URL of the dictionary file on GitHub
dictionary_url = "https://gist.githubusercontent.com/h3xx/1976236/raw/bbabb412261386673eff521dddbe1dc815373b1d/wiki-100k.txt"


# Function to fetch a random word from the dictionary
def fetch_random_word():
    response = requests.get(dictionary_url)

    if response.status_code == 200:
        words = response.text.splitlines()
        # Filter out lines containing non-alphabetic characters and special letters
        alphabetic_words = [word for word in words if
                            word.isalpha() and all(unicodedata.category(c) != 'Lo' for c in word)]
        random_word = random.choice(alphabetic_words)
        return random_word
    else:
        return "Failed to fetch word"


# Function to generate and display the sentence
def generate_sentence():
    new_word = fetch_random_word()
    current_sentence = sentence
    if current_sentence:
        updated_sentence = current_sentence + " " + new_word
    else:
        updated_sentence = new_word
    return updated_sentence


# Initialize an empty sentence
sentence = ""

# Fetch the dictionary file and filter out lines starting with '#!comment:'
response = requests.get(dictionary_url)
if response.status_code == 200:
    words = [line for line in response.text.splitlines() if not line.startswith('#!comment:')]
else:
    words = []

# Retro ASCII art header
header = """

 ██████╗  ██████╗ ██████╗     ███████╗ █████╗ ██╗   ██╗███████╗
██╔════╝ ██╔═══██╗██╔══██╗    ██╔════╝██╔══██╗╚██╗ ██╔╝██╔════╝
██║  ███╗██║   ██║██║  ██║    ███████╗███████║ ╚████╔╝ ███████╗
██║   ██║██║   ██║██║  ██║    ╚════██║██╔══██║  ╚██╔╝  ╚════██║
╚██████╔╝╚██████╔╝██████╔╝    ███████║██║  ██║   ██║   ███████║
 ╚═════╝  ╚═════╝ ╚═════╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝

Created by Hoso
____________________________________________
"""
# Display the header with a retro font and colors (adjust as needed)
os.system('cls' if os.name == 'nt' else 'clear')
print("\x1b[1;37m" + header + "\x1b[0m")  # Bright white text

# Display the initial message with green text for the specified part
print("\x1b[1;32mEnter to generate a new word and add to the sentence...\x1b[0m", end=" ")  # Green text

while True:
    user_input = input()
    if words:
        sentence = generate_sentence()
        # Clear the terminal screen before printing the new sentence
        os.system('cls' if os.name == 'nt' else 'clear')
        # Reprint the header
        print("\x1b[1;37m" + header + "\x1b[0m")
        # Wrap the sentence to a maximum line width of 80 characters (adjust as needed)
        wrapped_sentence = textwrap.fill(sentence, width=80)
        # White text for the sentence
        print("\x1b[1;37m" + wrapped_sentence + "\x1b[0m")
    else:
        # Retro red text for failure message
        print("\x1b[1;31mFailed to fetch words from the dictionary.\x1b[0m")
