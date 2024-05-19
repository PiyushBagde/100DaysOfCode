import pandas

student_df = pandas.DataFrame(pandas.read_csv('nato_phonetic_alphabet.csv'))

student_dict = {row.letter: row.code for (index, row) in student_df.iterrows()}


def generate_phonetic():
    user_input = input("Enter Name: ").upper()
    try:
        result = [student_dict[letter] for letter in user_input]
    except KeyError:
        print("onli, letters are acceptable")
        generate_phonetic()
    else:
        print(result)


generate_phonetic()
