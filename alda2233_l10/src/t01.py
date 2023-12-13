"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohamed
ID:      169072233
Email:   alda2233@mylaurier.ca
__updated__ = "2023-12-11"
-------------------------------------------------------
"""
# Imports
from asa import customer_record

fh = open("customers.txt", "r", encoding="utf-8")
n = int(input("record number"))
result = customer_record(fh, n)
print(result)
fh.close
