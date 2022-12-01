import pandas
df = pandas.read_csv("nato_phonetic_alphabet.csv")

student_data_frame = pandas.DataFrame(df)

new_dic = {row.letter: row.code for (
    index, row) in student_data_frame.iterrows()}

word = input("What would be the word? ").upper()

phonetic_list = [new_dic[letter] for letter in word]
print(phonetic_list)


# list_words = {word: key for value, key in new_dic.items()}

# new_word = []

# # for (key, value) in new_dic.items():
# #     if key == word:
# #         new_word.append(word, value)

# for letter in word:
#     if letter in new_dic:
#         a = letter, new_dic[letter]
#         new_word.append(a)
# print(new_word)
