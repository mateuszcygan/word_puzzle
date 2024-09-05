from collections import Counter


def check_guess(secret_word, guess):

    secret_word_length = len(secret_word)
    letters = list(secret_word)

    expected = []

    for x in range(secret_word_length):
        if secret_word[x] == guess[x]:
            expected.append("G")
            letters.remove(guess[x])
        elif guess[x] in letters:
            expected.append("Y")
            letters.remove(guess[x])
        else:
            expected.append("X")

    return expected


def guess_word(word_list, word_length, feedback_history):

    if len(feedback_history) == 0:

        # dictionary - letter at the correct position ('G'), list - letters that the secret word includes
        secret_word = {}
        secret_letters = []

        for i in word_length:
            secret_word[i] = None

        return word_list[0]
