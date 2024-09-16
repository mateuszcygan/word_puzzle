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

    num_of_words = len(word_list)
    x = len(feedback_history)

    if len(feedback_history) == 0:
        return word_list[0]

    # Extract the latest feedback word and its feedback
    feedback_word = feedback_history[-1][0]
    feedback = feedback_history[-1][1]

    feedback_word_length = len(feedback_word)

    # For each 'word' in the 'word_list'
    # Compare the letters of both words - taken word and word with feedback
    # If it is the same, depending on the feedback letters, decide what to do with words
    # THINK HOW TO AVOID COMPARING THE SAME WORD and in which cases it can occur
    for feedback_letter in feedback:
        for word in word_list:
            return


guess_word(["anana", "apple"], 5, [("apple", ["G", "G", "X", "G", "X"])])
