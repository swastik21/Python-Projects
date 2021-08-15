import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed_letters = []
    guessed_words = []
    tries = 6
    guessed = False
    print("Let's play hangmam!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word?: ").upper()
        if len(guess)==1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already have guessed that letter.")
            elif guess not in word:
                print(f"{guess} not in word")
                tries-=1
                guessed_letters.append(guess)
            else:
                print(f"{guess} is in the word")
                guessed_letters.append(guess)
                word_in_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_in_list[index] = guess
                word_completion = "".join(word_in_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess)==len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You have already guessed that word.")
            elif guess != word:
                print(f"{guess} is not the word")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = guess
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats!, you have guessed the word.")
    else:
        print(f"Sorry you ran out of tries, the word was {word}, maybe next time")

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("Do you want to play again?").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()
