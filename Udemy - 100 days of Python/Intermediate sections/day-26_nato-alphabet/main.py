# the following code receives a string and outputs it spelled using the nato phonetic alphabet

import pandas
NATO_CSV_FILEPATH = './Intermediate sections/day-26_nato-alphabet/nato_phonetic_alphabet.csv'

# convert the nato_phonetic_alphabet.csv file to a dataframe
df_nato = pandas.read_csv(NATO_CSV_FILEPATH)
# convert the dataframe to a dictionary, where each letter is a key and the corresponding code is the value
dict_nato = {row.letter:row.code for (index, row) in df_nato.iterrows()}
# receive string from user -> remove any spaces, because only characters will matter -> convert to uppercase
word_to_spell = input("Enter a word: ").replace(" ", "").upper()
# for each character, use the nato alphabet dictionary to find the corresponding code -> append this code to a result list
result = [dict_nato[char] for char in word_to_spell if char in dict_nato.keys()]
# output the result list
print(result)