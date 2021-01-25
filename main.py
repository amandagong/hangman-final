import random
import os
import no

words = ["bamboo", "cerulean", "mulch", "jeopardy", "attachment", "poker", "cornea", "trousers", "copper", "nevertheless","iron", "liberty", "ligaments", "elmo", "engine", "memory"]

def win():
  os.system("clear")
  print("you won.")
def lose():
  os.system("clear")
  print("you lose, no more body parts for you :(\nthe word was '%s'" % (word))
def setup():
  os.system("clear")
  print("input the words 'final guess' at any time to make a final guess. if you get those guesses wrong, you won't be remembered")
  print("current wrong guesses:")
  print(wrongguesses)
  print("you have %d body parts left" % (difficulty-len(wrongguesses)))
  print(displayedword)


word = random.choice(words)

wordlist = list(word)
displayedword = ("-"*len(word))
displayedlist = list(displayedword)
wrongguesses = []
print("you're getting hanged/slowly remembered? membered? disdismembered? like the opposite of dismembered\n\nguess letters or smth\n\nthe category is: things one can theoretically put in an eyeball socket, depending on willpower and intepretive abstraction\n")

difficulty = int(17 - int(input("Enter a difficulty from 1-10: ")))

while len(wrongguesses) < difficulty or displayedword != word:
  if displayedword == word:
    win()
    break
  elif len(wrongguesses) == difficulty:
    lose()
    break
  else:
    setup()
    guess = str(input("Guess a letter: ").lower)
    if guess == "final guess":
      final = str(input("Make your final guess: "))
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