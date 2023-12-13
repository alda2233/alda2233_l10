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

from functions import number_stats


with open('numbers.txt', 'r') as numbers_file:

    smallest, largest, total, average = number_stats(numbers_file)
    print(f"Smallest: {smallest}")
    print(f"Largest: {largest}")
    print(f"Total: {total:.2f}")
    print(f"Average: {average:.2f}")
