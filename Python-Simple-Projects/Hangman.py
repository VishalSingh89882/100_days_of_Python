import random
stages = ['''
  +---+
    |   |
    O   |
    /|\  |
    / \  |
    =========''', '''
  +---+
    |   |
    O   |
    /|\  |
    /    |
    =========''', '''
    +---+
    |   |
    O   |
    /|\  |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|   |
        |
    =========''', '''
    +---+
    |   |
    O   |
     |   |
        |
    =========''', '''  +---+
    |   |
    O   |
        |
        |
    =========''', '''  +---+
    |   |
        |
        |
        |
    =========''']


lives = 6
word_list=["python", "hangman", "challenge", "programming", "developer"]
chosen_word = random.choice(word_list)
print("Welcome to Hangman!")
print(chosen_word)
game_over = False
guessed_words = []
while not game_over:
    display = ""
    word = input("Guess a letter: ").lower()
    if word in guessed_words:
        print(f"You've already guessed {word}. Try again.")
    for letters in chosen_word:
        if letters == word:
            display += word
            guessed_words.append(word)
        elif letters in guessed_words:
            display += letters
        else:
            display += "_"
    
    if word not in chosen_word:
        print(f"You guessed {word}, that's not in the word. You lose a life.")
        lives -= 1
        print(f"You loose a life. Lives remaining: {lives}")
        if lives == 0:
            game_over = True
            print(f"The word was {chosen_word}. You lose.")

    print(display)
    if "_" not in display:
        game_over = True
        print("You win!")
    
    print(stages[lives])