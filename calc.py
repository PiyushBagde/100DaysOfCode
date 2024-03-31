logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)

def doCalculation(num1, num2, operation):
  if operation == "+":
    return num1 + num2 
  elif operation == "-":
    return num1 - num2
  elif operation == "/":
    return num1/num2
  elif operation == "*":
    return num1*num2
  else:
    return "Enter appropriate option"

num1 = float(input("What's your first number : "))
    
go_ahead = 'yes'
while go_ahead == 'yes':
  print('''
  +
  -
  /
  *
  ''')

  operation = input('Choose one of the operation from above : ')

  num2 = float(input("What's your second number : "))

  answer = doCalculation(num1, num2, operation)

  print(f'{num1} {operation} {num2} = {answer}')

  if input(f'Do you wanna play with the {answer}, say "yes" or "no" : ') == 'yes':
    num1 = answer
  else:
    go_ahead = "no"
  
  
