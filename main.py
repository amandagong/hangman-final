import random
import os


def win():
  os.system("clear")
  print("you won.")
def lose():
  os.system("clear")
  print("you lose, no more body parts for you :(")
def setup():
  os.system("clear")
  print("input the words 'final guess' at any time to make a final guess")
  print("current wrong guesses:")
  print(wrongguesses)
  print("you have %d body parts left" % (8-len(wrongguesses)))
  print(displayedword)

words = ["bamboo", "cerulean", "mulch", "jeopardy", "attachment", "poker", "cornea", "trousers", "copper", ""]
word = random.choice(words)
wordlist = list(word)
displayedword = ("-"*len(word))
displayedlist = list(displayedword)
wrongguesses = []

while len(wrongguesses) < 8 or displayedword != word:
  if displayedword == word:
    win()
    break
  elif len(wrongguesses) == 8:
    lose()
    break
  else:
    setup()
    guess = input("Guess a letter: ")
    if guess == "final guess":
      final = input("Make your final guess: ")
      if final == word:
        win()
        break
      else:
        setup()
    else:
      if len(guess) == 1 and guess not in wrongguesses:
        if guess in wordlist:
          for i in range(len(wordlist)):
            if wordlist[i] == guess:
              displayedlist[i] = guess
              displayedword = "".join(displayedlist)
          setup()
        else:
          if guess not in wrongguesses:
           wrongguesses.append(guess)
          setup()
      else:
        setup()