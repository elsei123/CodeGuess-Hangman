"""
Project: CodeGuess Hangman
Description: A word guessing game where the user tries to guess the secret word letter by letter
"""

import random

def get_random_word():
    """
    Get a random word and its hint from a predefined list.
    
    Returns:
        tuple: A tuple containing a randomly selected word and its hint.
    """
    # List of words and associated hints
    words_with_hints = [
        ('python', 'A popular programming language.'),
        ('hangman', 'A classic word-guessing game.'),
        ('challenge', 'Something that tests your abilities.'),
        ('programming', 'The process of writing computer code.'),
        ('openai', 'The organization that developed this model.'),
        ('algorithm', 'A step-by-step procedure for solving a problem.'),
        ('variable', 'A storage location identified by a memory address.'),
        ('function', 'A block of code that performs a specific task.'),
        ('debugging', 'The process of identifying and removing errors.'),
        ('syntax', 'The set of rules that defines the combinations of symbols.'),
        ('compiler', 'A program that translates code from high-level to machine language.'),
        ('loop', 'A sequence of instructions that is continually repeated.'),
        ('conditional', 'Statements that only run when a certain condition is true.'),
        ('recursion', 'When a function calls itself.'),
        ('array', 'A collection of items stored at contiguous memory locations.')
    ]
    # Randomly choose a word and its hint
    return random.choice(words_with_hints)

def display_word(word, guessed_letters):
    """
    Display the current state of the word with guessed letters.
    
    Args:
        word (str): The word to be guessed.
        guessed_letters (set): The set of letters that have been guessed correctly.
    
    Returns:
        str: The current state of the word with guessed letters and underscores for unguessed letters.
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
