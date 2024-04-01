
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
from random import randint

def deal_card():
  """Return a random card from deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  deck_length = len(cards)
  card =  cards[randint(0, deck_length-1)]
  return card


def calculate_score(cards):
  if len(cards) == 2 and sum(cards) == 21:
      return 0

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw 😒"
  elif computer_score == 0:
    return "Lose, opponent has a Blackjack"
  elif user_score == 0:
    return "you Win with Blackjack 😎"
  elif user_score > 21:
    return "You went over 🙄"
  elif computer_score > 21:
    return 'Opponent went over, you win 🥳'
  elif user_score > computer_score:
    return "You win 🎉"
  else:
    return "You loose 😢"
def play_game():
    users_card = [deal_card(), deal_card()]
    computers_card = [deal_card(), deal_card()]
    is_game_over = False

    while not is_game_over:
        user_score = calculate_score(users_card)
        computer_score = calculate_score(computers_card)

        print(f"  Your card {users_card}, current score :{calculate_score(users_card)}")

        print(f"  Computer's first card: {computers_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass : ")
            if another_card == 'y':
                users_card.append(deal_card())
            else:
                is_game_over = True


    while computer_score != 0 and computer_score < 17:
        computers_card.append(deal_card())
        computer_score = calculate_score(computers_card)

    print(f"your final hand :{users_card}, score : {user_score}")
    print(f"Computers final hand :{computers_card}, score : {computer_score}")

    print(compare(user_score, computer_score))

while input("Do you want to play the game type 'y' or 'n': ") =='y':
    print(logo)
    play_game()
