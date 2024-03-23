name_string = "Angela, Ben, Jenny, Michael, Chloe"

names = names_string.split(", ")

import random

index = random.randint(0, len(names)-1)
print(f"{names[index]} is going to buy the meal today!")
