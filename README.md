### Wordy Puzzle Game
Challange that comes from https://entwicklerheld.de/

This challenge is to implement the core logic of a word-guessing game. You will write two key functions:

check_guess: A function that evaluates a guessed word against a secret word and returns feedback in the form of G, Y, and X.
guess_word: A function that uses feedback from previous guesses to intelligently filter and select the next best guess from a list of possible words.
Once these functions are implemented, we will test them by simulating a complete game using the play_game function. The goal is to ensure that the game can accurately guess the secret word within a reasonable number of attempts.
