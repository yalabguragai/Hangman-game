import random

# words which are to be randomized by  the random module
words = ['People', 'Random', 'Church', 'Pakistan', 'Cricket', 'Terrorist', 'Prime', 'Gibbersh', 'English', 'heaven',
         'Environment', 'Matress', 'Electrification']


# function to return the word in upper case
def get_word():
    word = random.choice(words)
    return word.upper()


# funcion to address the main logic of the game
def play(word):
    word_list = ' _ ' * len(word)
    guessed = False
    guessed_letter = []
    guessed_word = []
    tries = 6
    print("lets start the hangman game!")
    print(stages_hangman(tries))
    print(word_list)
    print("\n")

    # main code for hangman game
    while not guessed and tries > 0:
        guess = input("please guess the word  \t").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letter:
                print('You have already entered the alphabet ', guess)
            elif guess not in word:
                print(guess, "is not the correct guess ")
                print("\n")
                tries -= 1
                guessed_letter.append(guess)
            else:
                print("Nice ", guess, "is is the corect guess")
                print("\n")
                guessed_letter.append(guess)
                word_as_list = list(word_list)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_list = "".join(word_as_list)

                if "_" not in word_list:
                    guessed = True


        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_word:
                print("you've already entered the word", guess)
                print("\n")
            elif guess != word:
                print(guess, "not in the word")
                print("\n")
                tries -= 1
                guessed_word.append(guess)
            else:
                guessed = True
                word_list = word

        else:
            print("please enter a valid alphabet")

        print(stages_hangman(tries))
        print(word_list)
      
      
      
    if guessed:
        print("congratulations,you have guessed the word")
        print("\n")
    else:
        print("Sorry you ran out of tries. The word was " + word + " .Better luck next time!")
        print("\n")


def stages_hangman(tries):
    phase = [
        # final phase with head two hands and two legs
        """
        --------------
        |           |
        |           O
        |          \\|/
        |           |
        |           /\\
        |
        |
        """,
        # phase with only one leg
        """
               --------------
               |           |
               |           O
               |          \\|/
               |           |
               |           /
               |
               |
        """,
        # phase without both legs
        """
               --------------
               |           |
               |           O
               |          \\|/
               |           |
               |           
               |
               |
        """,
        # phase without both legs and one hand
        """
               --------------
               |           |
               |           O
               |          \\|
               |           |
               |           
               |
               |
        """,
        # phase without both legs and hands
        """
               --------------
               |           |
               |           O
               |          |
               |           |
               |           
               |
               |
        """,
        # phase with only head
        """
               --------------
               |           |
               |           O
               |         
               |
               |
        """,
        # initial empty phase
        """
               --------------
               |           |
               |         
               |
               |
         """

    ]
    return phase[tries]


def main():
    word = get_word()
    play(word)
    while input("Do you want to play again? (Y/N) \t").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
