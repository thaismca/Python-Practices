# the following code receives a string and outputs it spelled using the nato phonetic alphabet

import pandas
NATO_CSV_FILEPATH = './Intermediate sections/day-26_nato-alphabet/nato_phonetic_alphabet.csv'

# TODO: convert the nato_phonetic_alphabet.csv file to a dataframe
df_nato = pandas.read_csv(NATO_CSV_FILEPATH)
# TODO: convert the dataframe to a dictionary, where each letter is a key and the corresponding code is the value
dict_nato = {row.letter:row.code for (index, row) in df_nato.iterrows()}
print(dict_nato)
# TODO: receive string from user -> remove any spaces, because only characters will matter -> convert to uppercase
word_to_spell = input("Enter a word: ").replace(" ", "").upper()
# TODO: convert string to list of characters
word_chars = [char for char in word_to_spell]
print(word_chars)
# TODO: for each character, use the nato alphabeth dictionary to find the corresponding code
        # TODO: append a string "{character} for {code}" to a result list
# TODO: output the result list