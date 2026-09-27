"""
CodeAlpha - Python Programming Internship
Task 1: Hangman Game

A simple text-based Hangman game.
- 5 predefined words
- Player guesses one letter at a time
- Max 6 incorrect guesses
"""

import random

WORDS = ["python", "hangman", "internship", "keyboard", "function"]
MAX_WRONG_GUESSES = 6

HANGMAN_STAGES = [
    """
       ------
       |    |
       |
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    ---------
    """,
]


def choose_word():
    return random.choice(WORDS)


def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def play_hangman():
    word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0

    print("Welcome to Hangman!")
    print(f"You have {MAX_WRONG_GUESSES} incorrect guesses allowed.\n")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print(HANGMAN_STAGES[wrong_guesses])
        print("Word: " + display_word(word, guessed_letters))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Incorrect guesses left: {MAX_WRONG_GUESSES - wrong_guesses}\n")

        if all(letter in guessed_letters for letter in word):
            print("🎉 Congratulations! You guessed the word: " + word)
            return

        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.\n")
        else:
            wrong_guesses += 1
            print(f"Wrong guess! '{guess}' is not in the word.\n")

    print(HANGMAN_STAGES[wrong_guesses])
    print(f"💀 Game over! The word was: {word}")


if __name__ == "__main__":
    play_again = "y"
    while play_again == "y":
        play_hangman()
        play_again = input("\nPlay again? (y/n): ").strip().lower()
    print("Thanks for playing Hangman!")
