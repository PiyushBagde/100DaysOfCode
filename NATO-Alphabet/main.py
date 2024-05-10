import pandas

student_df = pandas.DataFrame(pandas.read_csv('nato_phonetic_alphabet.csv'))

# TODO 1. Create a dictionary in this format:
student_dict = {row.letter: row.code for (index, row) in student_df.iterrows()}
# print(student_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter Name: ").upper()
result = [student_dict[letter] for letter in user_input]
print(result)
