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


def precompute_frequencies(words):
    frequency_map = {}
    for word in words:
        frequency_map[word[0]] = Counter(word[1])
    return frequency_map


def guess_word(word_list, word_length, feedback_history):

    for guess_word in word_list:
        expected = check_guess("secret", guess_word)
        feedback_history.append((guess_word, expected))

    frequency_map = precompute_frequencies(feedback_history)

    for key, counter in frequency_map.items():
        if counter("G") == 6:
            return key
        else:
            return None
