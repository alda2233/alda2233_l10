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
from functions import file_copy


with open('words.txt', 'r') as source_file:

    with open('new_words.txt', 'w') as target_file:

        file_copy(source_file, target_file)

print("Copying 'words.txt' to 'new_words.txt' completed.")
