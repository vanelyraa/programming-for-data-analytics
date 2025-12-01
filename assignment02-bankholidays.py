
# Assignment 2 - Bank holidays
# Author: Vanessa Lyra

'''Northern bank holdays'
Write a program called assignment02-bankholdiays.py
The program should print out the dates of the bank holidays that happen in northern Ireland.'''

#Part 1 - Print out NI Bank Holidays
import requests
#import json

year = "2025" #Choosing a year for analysis

# Bank holidays URL
url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()

# Getting NI bank holidays
bh_ni = data["northern-ireland"]["events"]

# Iterating through JSON and printing results
print("Northern Ireland bank holidays \n")
for item in bh_ni:
    if item["date"].startswith(year): #Finding all bank holidays from one specific year
        print(item["date"], item["title"]) #Printing each NI holiday

# Print each line of JSON data
#https://www.geeksforgeeks.org/python/loop-through-a-json-array-in-python/

# Startwith method
#https://www.w3schools.com/python/ref_string_startswith.asp 


'''Modify the program to print the bank holidays that are unique to northern Ireland (i.e. do not happen elsewhere in the UK) you can choose if you want to use the name 
or the date of the holiday to decide if it is unique.'''

#Part 2 - Print out unique NI Bank Holidays

# #Getting bank holidays by country
bh_england = data["england-and-wales"]["events"]
bh_scotland = data["scotland"]["events"]
bh_ni = data["northern-ireland"]["events"]

#Grouping all bank holidays from England and Scotland
other_bhs = {item["date"][5:] for item in bh_england} | {item["date"][5:] for item in bh_scotland}

#Iterating through NI bank holidays
print("\n Unique NI bank holidays \n")
for item in bh_ni:
    if item["date"].startswith(year) and item["date"][5:] not in other_bhs: #if the date doesn't exist in the England/Scotland group created
        print(item["date"], item["title"]) #Print the unique bank holiday


# https://www.w3schools.com/python/ref_set_union.asp union operator
# https://www.freecodecamp.org/news/python-slicing-how-to-slice-an-array/ Slicing method