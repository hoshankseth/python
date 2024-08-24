import pandas as pd

nato_alphabet = pd.read_csv("NATO-alphabet-start/NATO-alphabet-start/nato_phonetic_alphabet.csv")
print(nato_alphabet.head())

# for (index, row) in nato_alphabet.iterrow():

# nato_alphabet['letter']
nato_dict = {letter:code for (letter,code) in nato_alphabet.iterrows()}
print(nato_dict)