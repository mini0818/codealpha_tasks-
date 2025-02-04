import random

# Hangman ASCII Art Stages
hangman_stages = [
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / 
       |
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |    
       |
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |    
       |
    """,
    """
       ------
       |    |
       |    O
       |    |
       |    
       |
    """,
    """
       ------
       |    |
       |    O
       |    
       |    
       |
    """,
    """
       ------
       |    |
       |    
       |    
       |    
       |
    """
]

# Word list
words = ["python", "hangman", "computer", "programming", "developer"]
word = random.choice(words)
guessed_word = ["_"] * len(word)
attempts = len(hangman_stages) - 1
guessed_letters = set()

print("Welcome to Hangman!")
print(" ".join(guessed_word))

while attempts > 0 and "_" in guessed_word:
    guess = input("\nGuess a letter: ").lower()
    
    if guess in guessed_letters:
        print("You've already guessed that letter! Try again.")
        continue
    
    guessed_letters.add(guess)
    
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed_word[i] = guess
    else:
        attempts -= 1
    
    print(hangman_stages[attempts])
    print(" ".join(guessed_word))
    
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word!")
else:
    print(f"\nGame over! The word was '{word}'. Better luck next time!")

