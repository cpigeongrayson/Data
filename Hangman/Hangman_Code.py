import Random_Words
import Hangman_Functions

def play_hangman(difficulty):
    """Plays one game of Hangman with the user."""
    # Sets player lives.
    lives = 6

    # Retrieves a random word from Random Words.
    word = Hangman_Functions.get_word(difficulty)

    # Hides the word from the user.
    hidden_word = Hangman_Functions.hide_letters(word)

    list_of_guesses = []

    while lives > 0:
        # Asks the user's guess and stores it as guess, while adding it to the list of guessed words. 
        guess = input("What letter would you like to guess? ").strip().lower()
        
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
                    ]

        # Checks if guess is a letter of the english alphabet.
        if guess not in alphabet:
             print("Please guess a letter of the alphabet.")
             print("")
             continue

        # Checks if guess has already been guessed.
        elif guess in list_of_guesses:
             print(f"You have already guessed the letter: {guess}. Try again!")
             print("")
             continue
        
        # Adds guess to list of guessed letters.
        Hangman_Functions.letter_guessed(guess, list_of_guesses)

        # Checks if the player's guess is contained in the word.
        guess_true = Hangman_Functions.play_round(word, guess)

        # If the player's guess is contained within the word, the place of the letter in the word is revealed.
        if guess_true:
            hidden_word = Hangman_Functions.show_letter(guess, hidden_word, word)
        # If not, the player looses a life.
        else:
            lives -= 1
        
        # Checks to see if the player has won the game.
        if Hangman_Functions.did_player_win(word, hidden_word):
                print(f"You have correctly guessed the word {word}!")
                break

        Hangman_Functions.display_game_info(lives, list_of_guesses, hidden_word)
    
    # Checks to make sure the player is still alive in the game.
    if lives == 0:
            print(f"You have no more lives left. The word was {word}")

game_online = True

if game_online == True:
    while True:
        # Allows user to set a valid difficulty.
        difficulty = input("Please select your game's difficulty (easy, medium, hard): ").strip().lower()
        if difficulty not in ["easy", "medium", "hard", "nightmare"]:
             print("That is not a valid difficulty level. Please try again!")
             continue
        
        # Plays one game of Hangman.
        play_hangman(difficulty)

        # Allows user to decide whether or not they'd like to continue playing.
        play_again = input("Would you like to play another game of Hangman? (yes/no): ").strip().lower()
        # If user decides to stop playing Hangman, the game shuts down.
        if play_again not in ["yes", "y"]:
            print("Thanks for playing Hangman!")
            break