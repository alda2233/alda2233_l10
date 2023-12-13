"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohamed
ID:      169072233
Email:   alda2233@mylaurier.ca
__updated__ = "2023-11-23"
-------------------------------------------------------
"""
# Imports
from functions import count_frequency_word


with open('words.txt', 'r') as words_file:

    search_word = input("Word to count: ")

    count = count_frequency_word(words_file, search_word)

    print(f"'{search_word}' appears {count} time(s)")
