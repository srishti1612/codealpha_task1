import random

# List of possible words
word_list = ['python', 'hangman', 'programming', 'developer', 'algorithm', 'challenge','designer']

# Select a random word
selected_word = random.choice(word_list)
word_length = len(selected_word)
guessed_word = ['_'] * word_length
guessed_letters = set()
max_attempts = 6
attempts = 0

print("Welcome to Hangman!")
print("Guess the word: " + ' '.join(guessed_word))

while attempts < max_attempts and '_' in guessed_word:
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabetical letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in selected_word:
        for index, letter in enumerate(selected_word):
            if letter == guess:
                guessed_word[index] = guess
        print("Good job!")
    else:
        attempts += 1
        print(f"Wrong guess. Attempts remaining: {max_attempts - attempts}")

    print(' '.join(guessed_word))

# Game over message
if '_' not in guessed_word:
    print("Congratulations! You guessed the word:", selected_word)
else:
    print("Game over. The word was:", selected_word)
