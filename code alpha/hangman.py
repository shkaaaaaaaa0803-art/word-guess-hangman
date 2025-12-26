import random

def play_hangman():
    
    word_bank = {
        'python': 'A popular high-level programming language.',
        'algorithm': 'A set of steps to solve a specific problem.',
        'variable': 'A container for storing data values.',
        'boolean': 'A data type that has one of two possible values.',
        'compiler': 'Translates code into machine language.'
    }

    target_word = random.choice(list(word_bank.keys()))
    clue = word_bank[target_word]
    
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6
    
    print("--- Welcome to Hangman! ---")
    print(f"CLUE: {clue}")

    while incorrect_guesses < max_attempts:
        # Display logic
        display_word = ""
        for letter in target_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"\nWord: {display_word}")
        print(f"Attempts left: {max_attempts - incorrect_guesses}")
        
        if "_" not in display_word:
            print(f"Congratulations! You guessed the word: {target_word}")
            break

        
        print("Type a letter or type 'hint' to reveal a letter (costs 2 attempts)")
        user_input = input("Your move: ").lower().strip()

        
        if user_input == 'hint':
            if (max_attempts - incorrect_guesses) <= 2:
                print("Not enough attempts left to buy a hint!")
            else:
                # Find all letters in the word that haven't been guessed yet
                remaining_letters = [l for l in target_word if l not in guessed_letters]
                if remaining_letters:
                    bought_letter = random.choice(remaining_letters)
                    guessed_letters.append(bought_letter)
                    incorrect_guesses += 2
                    print(f"HINT: The letter '{bought_letter}' has been revealed. (-2 attempts)")
            continue

        
        if len(user_input) != 1 or not user_input.isalpha():
            print("Please enter a single letter.")
            continue
        
        if user_input in guessed_letters:
            print(f"You've already tried '{user_input}'.")
            continue

        guessed_letters.append(user_input)

        
        if user_input in target_word:
            print(f"Correct! '{user_input}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{user_input}' is not there.")

    if incorrect_guesses >= max_attempts:
        print("\n--- Game Over ---")
        print(f"Out of lives! The word was: {target_word}")

    print("\nThank you for playing this game!")

if __name__ == "__main__":
    play_hangman()
