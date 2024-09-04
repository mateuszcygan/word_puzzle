from task import check_guess, guess_word


def play_game(secret_word, word_list, output):
    attempts = len(word_list)
    feedback_history = []

    output.append(f"The secret word has {len(secret_word)} letters.")

    for attempt in range(attempts):
        guess = guess_word(word_list, len(secret_word), feedback_history)

        if guess is None or len(guess) != len(secret_word):
            output.append(
                f"Guess {attempt + 1}/{attempts}: Please enter a word with {len(secret_word)} letters."
            )
            continue

        feedback = check_guess(secret_word, guess)
        feedback_history.append((guess, feedback))
        output.append(
            f"Guess {attempt + 1}/{attempts}: {guess} -> {' '.join(feedback)}"
        )

        if guess == secret_word:
            output.append("Congratulations, you guessed the word!")
            return True

    output.append(f"Sorry, you lost. The correct word was: {secret_word}")
    return False
