import random

def choose_word():
    with open("words.txt", "r") as file:
        words = file.read().splitlines()
    return random.choice(words).lower()

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def get_guess(guessed_letters):
    while True:
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter.")
        else:
            return guess

def play_game():
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    print("Welcome to Hangman!")

    while True:
        print("\nWord:", display_word(word, guessed_letters))
        print("Guessed letters:", ' '.join(guessed_letters))
        print(f"Remaining attempts: {max_attempts - incorrect_guesses}")

        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
        else:
            print("Wrong!")
            incorrect_guesses += 1

        if all(letter in guessed_letters for letter in word):
            print("\n:) You won! The word was:", word)
            break
        elif incorrect_guesses >= max_attempts:
            print("\n:( Game over! The word was:", word)
            break

if __name__ == "__main__":
    play_game()
