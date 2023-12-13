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

from functions import customer_append


with open('customers.txt', 'a') as customers_file:

    customer_data = input(
        "Enter customer data (ID, First Name, Last Name, Balance, Date): ").split(',')

    customer_append(customers_file, customer_data)

    print("Data appended to file.")
