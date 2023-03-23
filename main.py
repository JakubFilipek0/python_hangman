import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

lives = 6

print(hangman_art.logo)
print(f"Word to guess (testing): {chosen_word}")

while "_" in display:
    print(hangman_art.stages[lives])
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed letter '{guess}'")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"Letter '{guess}' is not in word to guess")
        lives -= 1
        if lives <= 0:
            print(hangman_art.stages[lives])
            print(f"You lose. Word was '{chosen_word}'")
            break

    print(display)
    print(f"Lives {lives}")

if "_" not in display:
    print(f"You win. Word was '{chosen_word}'")
