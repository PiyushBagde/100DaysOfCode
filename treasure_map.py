line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?

letter = ['A','B','C']

col = letter.index(position[0])
row = int(position[1])

map[row-1][col] = 'X'

print(f"{line1}\n{line2}\n{line3}")
