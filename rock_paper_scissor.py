rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

user_choice = int(input("Your Choice : type 0 for rock, 1 for paper, 2 for scissor ..."))

gesture = [rock ,paper, scissors]

print(gesture[user_choice])

computer_choice = random.randint(0,2)

print(gesture[computer_choice])

if user_choice == computer_choice:
  print("Its a draw")
else:
  if user_choice == 0:
    if computer_choice == 1:
      print("computer wins")
    else:
      print("You wins")
      
  elif user_choice == 1:
    if computer_choice == 2:
      print("computer wins")
    else:
      print("You wins")
  else:
    if computer_choice == 0:
      print('coputer wins')
    else:
      print('You wins')
  
