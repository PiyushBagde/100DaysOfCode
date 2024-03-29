from replit import clear # have to manage with this , clear screen for as the new bidders gat added
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


print(logo)

bidders = {}

other_bidders = 'yes'

while other_bidders == 'yes':
  
  name = input("What is your name? : ")
  bid = int(input("What's your bid? : $ "))

  bidders[name] = bid
  
  other_bidders = input("Are there any ohter bidders ? Type 'yes or no' : ")
  clear()

winner = ""
highest_bid = 0

for name in bidders:
  if bidders[name] > highest_bid:
    winner = name
    highest_bid = bidders[name]

print(f"The winner is {winner} with a highest bid ${highest_bid}.")
