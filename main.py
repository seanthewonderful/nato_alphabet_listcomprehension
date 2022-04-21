student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

from encodings import search_function
import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

with open("nato_phonetic_alphabet.csv"):
    nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
    nato_df = pandas.DataFrame(nato_data)

nato_dict = {row.letter:row.code for (index, row) in nato_df.iterrows()}

# print(nato_dict.items())

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_nato():
    word = input("Enter word: ").upper()
    try:
        phonetic = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Please enter only characters from the superiour Englishe Alphabette")
        generate_nato()
    else:
        print(phonetic)
        generate_nato()

generate_nato()

"""
append the value from nato_dict where the value's key is the letter[i] in word
"""