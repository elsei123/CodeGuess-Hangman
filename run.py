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