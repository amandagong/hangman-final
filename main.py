import random
import os

def win():
  os.system("clear")
  print("you won")
def lose():
  print("you lose")

words = ["protist", "jeopardy", "attachment", "poker", "bamboo", "crustacean", "cerulean", "mulch", "cornea"]
word = random.choice(words)
wordlist = list(word)
displayedword = ("-"*len(word))
displayedlist = list(displayedword)
wrongguesses = []

print("input the words 'final guess' at any time to make a final guess")



while len(wrongguesses) < 8 or displayedword != word:
  print("you have %d body parts left" % (8-len(wrongguesses)))
  print(displayedword)
  guess = str(input("Guess a letter: "))
  if guess == "final guess":
    final = input("Make your final guess: ")
    if final == str(word):
      win()
    else:
      "wrong."
  else:
    if displayedword == word:
      win()
    elif len(guess) == 1 and guess not in wrongguesses:
      for i in wordlist:
        if guess in wordlist:
         foundindex = wordlist.index(guess)
         displayedlist[foundindex] = guess
         displayedword = "".join(displayedlist)
        else:
          if guess not in wrongguesses:
           wrongguesses.append(guess)
           print("wrong guess. current wrong guesses:")
           print(wrongguesses)
    else:
      print("you already chose that letter or that is not a letter")
lose()