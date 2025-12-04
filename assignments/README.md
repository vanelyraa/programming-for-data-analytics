# programming-for-data-analytics

# Programming for Data Analytics Assessment

## Table of Contents
 - [Project Purpose](#project-purpose)
 - [Setup Instructions](#setup-instructions)
 - [Install Dependencies](#install-dependencies)
 - [Implementations](#implementations)
    - [Assignment 2](#assignments/assignment02-bankholidays.py)
    - [Assignment 3](#assignments/assignment03-pie.ipynb)
    - [Assignment 5](#assignment05-population.ipynb)
    - [Assignment 6](#assignment06-weather.ipynb)

## Project Purpose
This repository contains my assignments and project submissions for the Programming for Data Analytics module completed as part of the Higher Diploma in Science in Computing in Data Analytics at ATU.
The goal of this project is to demonstrate my skills in: python programming, data retrieval from various sources (URLs, CSV files, JSON), data cleaning and analysis, data manipulation with pandas, data visualisation using matplotlib and seaborn, and statistics calculations such as mean.

## Install Dependencies
All required libraries are listed in requirements.txt  

## Setup Instructions
Clone this GitHub repository:
<pre> git clone https://github.com/vanelyraa/programming-for-data-analytics.git </pre>

Navigate the project directory:
<pre> cd https://github.com/vanelyraa/programming-for-data-analytics.git </pre>

Create a virtual environment (optional):
<pre> python3 -m venv venv </pre>

Activate virtual environment (optional):  
For windows: <pre> source venv/bin/activate </pre> 
For MacOS: <pre> source venv/bin/activate  </pre> 

Install required dependencies:
<pre> pip install -r requirements.txt </pre>

## Implementations

#### Assignment 2 – Bank Holidays

The assignment is divided into two parts:

In part 1 we are required to print out Northern Ireland's bank holidays. First a variable year is defined. The script begins sending a request to [Gov.uk](https://www.gov.uk/bank-holidays.json) and fecth data using [Requests](https://requests.readthedocs.io/?utm_source=chatgpt.com) library. The data is saved in a dictionary called "data", the bank holidays are separated by region: Northern Ireland, England and Wales and Scotland, each region has his own set of bank holidays under events and each bank holiday is a dictionary with date and title.
A variable called "bh_ni" is created to store Northern Ireland's holidays accessing dictionaries "northern-ireland" and "events" stored previously in "data". A print statement "Northern Ireland bank holidays" is printed out to user. The program loops through "bh_ni" usng a for loop, first checking if the dates start with the previouly chosen year. If they do, the program will print the holiday date and title, showing all Northern Ireland bank holidays.
The "year" variable was added to prevent holidays from being duplicated since the data contains bank holidays from multiple years.

In part 2, we are required to print out bank holidays that are unique to Northern Ireland. Three lists are created: bh_ni, bh_england and bh_scotland to store bank holidays for each region by accessing the respective region and "events". The program combines the dates from "bh_england" and "bh_scotland", using month and day, the year part of the dates are "ignored" using slicing , the results are stored in variable called "other_bhs". The script then loops throught "bh_ni", checking first if the dates start with the previouly chosen year and whether the dates (again striped of year) are not showing in "other_bhs". If both conditions are met, the holiday is printed to user.


#### Assignment 3 - Pie

In this exercise we are required to plot a pie chart of 1000 people's email domains. The code is written in a Python notebook and uses [pandas](https://pandas.pydata.org/docs/) and [matplotlib.pyplot](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html) libraries.
The program begins reading the data from a CSV file hosted on Google Drive and storing in a [Dataframe](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) called "df". 
A new column called Domain is created in the DataFrame to stores each email domain. The domain on its own is obtained by splitting the email adress string from column "email" at "@" character using ".str.split" and ".str[1]" keeps only the element at index 1 which are the domains.
A variable called counting_domains is created to store the number of occurrences of each unique domain calculated by using pandas [value_counts()](https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html)".
The pie plot then is created using matplotlib [plot.pie](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.pie.html) with counting_domains as its variable variable. A title is added to the plot, and y-axis label is hidden for better visualisation

#### Assignment 5 - Population

The program is written in a Jupiter notebook and performs required analysis of the difference between sexes by age using official population data from Ireland. The assignment is divided into three parts:

For Part 1 we are required to calculate: weighted mean age (by sex) and difference between the sexes by age. The script starts by first reading and storing the data in a DataFrame "df" and headers are printed out to user for reference. All unnecessary columns are dropped using ".drop". The column containing age data "Single Year of Age" is cleaned by replacing text such as "Under 1 year" with zero using ".replace" and ensuring colunm only contain integers with "astype('int64')". The column "VALUE" which is the population count is also converted integer.
After the data is properly cleaned, it is reorganized with a pandas [pivot table](https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html), stored in a new DataFrame "df_anal" where the rows corresponds to "Single Year of Age" and columns female and male population. 


#### Assignment 6 - Weather

** End **



