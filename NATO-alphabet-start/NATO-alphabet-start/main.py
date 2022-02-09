import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_nato_callback():

    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only single words are accepted. Only letters from the alphabet are accepted. "
              "Please try again.")
        generate_nato_callback()
    else:
        print(output_list)


generate_nato_callback()
