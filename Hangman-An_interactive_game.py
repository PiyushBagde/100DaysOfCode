print('Welcome to the')
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/               
                   
                   
                   ''')

print("\nBefore staring let's put some light on the rules: ")

print('''
One player thinks of a word.
The other player guesses letters to uncover the word.
Correct guesses reveal letters in their correct positions.
Incorrect guesses result in drawing parts of a gallows and a hanging man.
The game continues until the word is guessed correctly or too many incorrect guesses are made, resulting in a loss.


''')

print("LET's Start playing already:\n")
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


import random
word_list = ["aardvark", "baboon", "camel", "beekeeper","pneumonia","fluffiness","knapsack","buzz","giggle","snowflakes"]

lives = 6

word = word_list[random.randint(0,len(word_list)-1)]
word2 = word

word_length = len(word)

guessing = ["_"] * word_length

end_of_game = False

while not end_of_game:
  guess = input("What could be the letter ? ").lower()

  if guess in word and guess in word2:
    for index, letter in enumerate(word):
      if guess == letter:
        guessing[index] = guess
    word2 = word2.replace(guess, "")

  else:
    print(stages[lives])
    lives -= 1
  print(guessing)
  print('\n')

  if "_" not in guessing:
    end_of_game = True
    print('You win!!!')
  elif lives == -1:
    end_of_game = True
    print('Yoy loss :|')

