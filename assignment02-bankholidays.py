
# Assignment 2 - Bank holidays
# Author: Vanessa Lyra

'''Northern bank holdays'
Write a program called assignment02-bankholdiays.py
The program should print out the dates of the bank holidays that happen in northern Ireland.
Last few marks (ie this is more tricky)
Modify the program to print the bank holidays that are unique to northern Ireland (i.e. do not happen elsewhere in the UK) you can choose if you want to use the name 
or the date of the holiday to decide if it is unique.'''

#Part 1 - Print out NI Bank Holidays
import requests
#import json

# Bank holidays URL
url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()

#Getting NI bank holidays
bank_holidays_ni = data["northern-ireland"]["events"]

#Iterating through JSON and printing results
for item in bank_holidays_ni:
    print(item["date"], item["title"])

# Print each line of JSON data
https://www.geeksforgeeks.org/python/loop-through-a-json-array-in-python/

