print("The Love Calculator is calculating your score...")
name1 = input('What is your name?') 
name2 = input('What is their name?') 

combined_name = name1 + name2

t = (combined_name.lower()).count("t")
r = (combined_name.lower()).count("r")
u = (combined_name.lower()).count("u")
e = (combined_name.lower()).count("e")


l = (combined_name.lower()).count("l")
o = (combined_name.lower()).count("o")
v = (combined_name.lower()).count("v")
e = (combined_name.lower()).count("e")

first_digit = t+r+u+e
second_digit = l+o+v+e

score = int(str(first_digit)+str(second_digit))
if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score< 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
  



