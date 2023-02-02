import random
from words import words
import string

def get_valid_words(words):
    word = random.choice(words)

    # choose a word without '-' and spaces
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_words(words)
    word_letters = set(word) # scrambling letters
    alphabet = set(string.ascii_uppercase) # creating a set of an alphabet
    used_letters = set() # what the user has guessed or typed

    lives = 6

    while len(word_letters) > 0 and lives > 0:
      print("You have", lives, "Letters that you already used: ", " ".join(used_letters))

      word_list = [letter if letter in used_letters else "-" for letter in word] # ["a", "b", "c"]
      print("Current word: ", " ".join(word_list))

      user_letter = input("Guess a letter: ").upper()


      if user_letter in alphabet - used_letters: 
            used_letters.add(user_letter)
            if user_letter in word_letters:
              word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("Letter is not valid in word.")
      elif user_letter in used_letters:
          print("You have already used that character. Please try again.")
      else:
          print("You have entered an invalid character. Please try again.")

    if lives == 0:
        print("You died, the word was, ", word)
    else:
        print("You guessed the word, ", word, "!!")
    
hangman()