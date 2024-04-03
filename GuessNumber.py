logo = '''
  /$$$$$$                                                 /$$     /$$                       /$$   /$$                         /$$                          
 /$$__  $$                                               | $$    | $$                      | $$$ | $$                        | $$                          
| $$  \__/ /$$   /$$  /$$$$$$   /$$$$$$$ /$$$$$$$       /$$$$$$  | $$$$$$$   /$$$$$$       | $$$$| $$ /$$   /$$ /$$$$$$/$$$$ | $$$$$$$   /$$$$$$   /$$$$$$ 
| $$ /$$$$| $$  | $$ /$$__  $$ /$$_____//$$_____/      |_  $$_/  | $$__  $$ /$$__  $$      | $$ $$ $$| $$  | $$| $$_  $$_  $$| $$__  $$ /$$__  $$ /$$__  $$
| $$|_  $$| $$  | $$| $$$$$$$$|  $$$$$$|  $$$$$$         | $$    | $$  \ $$| $$$$$$$$      | $$  $$$$| $$  | $$| $$ \ $$ \ $$| $$  \ $$| $$$$$$$$| $$  \__/
| $$  \ $$| $$  | $$| $$_____/ \____  $$\____  $$        | $$ /$$| $$  | $$| $$_____/      | $$\  $$$| $$  | $$| $$ | $$ | $$| $$  | $$| $$_____/| $$      
|  $$$$$$/|  $$$$$$/|  $$$$$$$ /$$$$$$$//$$$$$$$/        |  $$$$/| $$  | $$|  $$$$$$$      | $$ \  $$|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$$| $$      
 \______/  \______/  \_______/|_______/|_______/          \___/  |__/  |__/ \_______/      |__/  \__/ \______/ |__/ |__/ |__/|_______/  \_______/|__/      
'''

from random import randint

def start_game():
  print('Welcome to the Number Guessing Game !')
  print("I'm thinking about the number between 1 & 100 : ")
  
def make_guess():
  '''Return a number from 1 - 100 '''
  return randint(2,99)

def player_turn():
  global attempts
  user_guess = int(input("Make a guess : "))
  attempts -= 1
  if attempts == 0:
    print('You have run out of attempts. Better luck next time! 👍🏻')
  elif user_guess == orginal_number:
    print(f"You got it ! The answer was {user_guess}")
  elif user_guess < orginal_number :
    print("Too low")
    print(f"You have {attempts} left\n ")
    
    print('Guess again')
    player_turn()
  else:
    print("Too High")
    print('Guess again')
    print(f"You have {attempts} left\n ")
    
    player_turn()
  

# greetings and guess to start
print(logo)
start_game()

orginal_number = make_guess()
# print(f"The correct answer is {orginal_number}")

print("Can you get into my mind ? letss check it out !\n")

difficulut_level = input("Select your difficulty level 'easy' or 'hard' : ")

attempts = 10 if difficulut_level == 'easy' else 5

player_turn()
