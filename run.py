"""
Project: CodeGuess Hangman
Description: A word guessing game where the user tries to guess the secret word letter by letter
"""

import random

def get_random_word():
    """
    Get a random word from a predefined list.
    """
    words = ['python', 'hangman', 'challenge', 'programming', 'openai']
    return random.choice(words)


def display_word(word, guessed_letters):
    """
    Display the current state of the word with guessed letters.
    """
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])


def play_game():
    """
    Main function to play the game.
    """
    word = get_random_word()
    guessed_letters = set()
    attempts = 6
    