
import pandas as pd

data = pd.read_csv("NATO-alphabet-start/nato_phonetic_alphabet.csv")

# for row,col in data.iterrows():
#     print(row)
#     print(col.letter)
#     print(col.code)

#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)