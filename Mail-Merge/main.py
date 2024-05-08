PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()

with open("./Input/Letters/starting_letter.txt") as file:
    txt = file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = txt.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode='w') as letter:
            letter.write(new_letter)
