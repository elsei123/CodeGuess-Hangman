"""
Project: CodeGuess Hangman
Description: A word guessing game where the user tries to guess the secret word letter by letter
"""

import random

def get_random_word():
    """
    Get a random word from a predefined list.
    
    Returns:
        str: A randomly selected word from the predefined list.
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

    print("Welcome to Hangman!")

    while attempts > 0 and set(word) != guessed_letters:
        print(f"Word: {display_word(word, guessed_letters)}")
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Correct!")
        else:
            attempts -= 1
            print("Incorrect!")

    if set(word) == guessed_letters:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    play_game()
