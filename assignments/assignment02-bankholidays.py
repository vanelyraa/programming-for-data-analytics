
# Assignment 2 - Bank holidays
# Author: Vanessa Lyra

# Northern bank holdays  
# Write a program called assignment02-bankholdiays.py
# The program should print out the dates of the bank holidays that happen in northern Ireland

#Part 1 - Print out NI Bank Holidays

# Importing libraries
import requests

# Choosing a year for analysis, data contains multiple years, defining a year will prevent the code to print the same BH multiple times
year = "2025" 

# Bank holidays URL
url = "https://www.gov.uk/bank-holidays.json"

# Sending requet to API and converting data into Python dictionary
response = requests.get(url)
data = response.json()

# Getting NI bank holidays from events column and storing them
bh_ni = data["northern-ireland"]["events"]

# Iterating through bh_ni and printing NI bank holiday dates 
print("Northern Ireland's bank holiday dates \n")
for item in bh_ni:
    if item["date"].startswith(year): #Finding all bank holidays from one specific year
        print(item["date"]) #Printing each BH date


# Print each line of JSON data
# https://www.geeksforgeeks.org/python/loop-through-a-json-array-in-python/

# Startswith method
#https://www.w3schools.com/python/ref_string_startswith.asp 


# Modify the program to print the bank holidays that are unique to northern Ireland (i.e. do not happen elsewhere in the UK) 
# you can choose if you want to use the name or the date of the holiday to decide if it is unique.



# Part 2 - Print out unique NI Bank Holidays

# Getting bank holidays by country from column events
bh_england = data["england-and-wales"]["events"]
bh_scotland = data["scotland"]["events"]
bh_ni = data["northern-ireland"]["events"]

# Grouping all bank holidays from England and Scotland into one variable, excluding the year portion of the dates with slicing 
other_bhs = {item["date"][5:] for item in bh_england} | {item["date"][5:] for item in bh_scotland}

# Iterating through NI bank holidays
# Print statement to user
print("\n Unique NI bank holidays \n")
# For loop iterates through NI bank holidays from pre-defined year, ignore the year portion of the dates
# And look for dates that are not included in "other_bhs" which contains England and Scotlands BHs
for item in bh_ni:
    if item["date"].startswith(year) and item["date"][5:] not in other_bhs: 
        print(item["date"], item["title"]) # Print the unique bank holidays

# Union operator
# https://www.w3schools.com/python/ref_set_union.asp 

# Slicing method
# https://www.freecodecamp.org/news/python-slicing-how-to-slice-an-array/ 