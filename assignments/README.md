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
This repository contains my assignment submissions for the Programming for Data Analytics module completed as part of the Higher Diploma in Science in Computing in Data Analytics at ATU.

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

In part 1, we are required to print out Northern Ireland's bank holidays. First, a variable year is defined. The script begins sending a request to [Gov.uk](https://www.gov.uk/bank-holidays.json) and fetch data using [Requests](https://requests.readthedocs.io/?utm_source=chatgpt.com) library. The data is saved in a dictionary called "data", the bank holidays are separated by region: Northern Ireland, England and Wales and Scotland, each region has its own set of bank holidays under events and each bank holiday is a dictionary with date and title.
A variable called "bh_ni" is created to store Northern Ireland's holidays, accessing dictionaries "northern-ireland" and "events" previously stored  in "data". The program loops through "bh_ni" usng a for loop, first checking if the dates start with the previously chosen year. If they do, the program will print the holiday date and title, showing all Northern Ireland bank holiday dates.
The "year" variable was added to prevent duplicated holidays, since the data contains bank holidays from multiple years.

In part 2, we are required to print out bank holidays that are unique to Northern Ireland. Three lists are created: bh_ni, bh_england and bh_scotland to store bank holidays for each region by accessing the respective region and "events". The program combines the dates from "bh_england" and "bh_scotland", using month and day, the year is "ignored" using slicing, the results are stored in a variable called "other_bhs". The script then loops through "bh_ni", checking first if the dates start with the previously chosen year and whether the dates (again year is ignored using slicing) are not showing in "other_bhs". If both conditions are met, the holiday is printed to user.


#### Assignment 3 - Pie

In this exercise, we are required to plot a pie chart of 1000 people's email domains. The code is written in a Python notebook and uses [pandas](https://pandas.pydata.org/docs/) and [matplotlib.pyplot](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html) libraries.
The program begins reading the data from a CSV file hosted on Google Drive and storing it in a [Dataframe](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) called "df". 
A new column called Domain is created in the DataFrame to store each email domain. The domain on its own is obtained by splitting the email address string from column "email" at "@" character using ".str.split", and ".str[1]" accesses only the element at index 1, which is the domain.
A variable called counting_domains is created to store the number of occurrences of each unique domain calculated by using pandas [value_counts()](https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html)".
The pie plot then is created using matplotlib [plot.pie](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.pie.html) with counting_domains as its variable. A title is added to the plot, and y-axis label is hidden for better visualisation.
The pie slices are displayed in defined blue colours, the largest slice example.org is separated (exploded) for the chart, result percentages were added, a shadow with determined edgecolor and darkness, labels were removed.
The domains are displayed in legend and positioned using bbox_to_anchor and loc functions.


#### Assignment 5 - Population

The program is written in a Jupiter notebook and performs required analysis of the difference between sexes by age using official population data from Ireland. The assignment is divided into three parts:

For Part 1 we are required to calculate: weighted mean age (by sex) and difference between the sexes by age. The script starts by first reading and storing the data in a DataFrame "df" and headers are printed out to user for reference. All unnecessary columns are dropped using ".drop". To guarantee correct calculations, the data is filtered to use only Ireland in Administrative Counties, is used  The column containing age data "Single Year of Age" is cleaned by replacing text such as "Under 1 year" with zero using ".replace" and ensuring colunm only contains integers with "astype('int64')". The column "VALUE" which is the population count is also converted integer.
After the data is properly cleaned, it is reorganised with a pandas [pivot table](https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html), stored in a new DataFrame "df_anal" where each row shows an age from "Single Year of Age", and the columns contain the population of male and female for that same age.
The weighted mean age by sex is calculated using [numpy.average](https://numpy.org/doc/2.3/reference/generated/numpy.average.html) where "Single Year of Age" is the array and sexes are the weighted values, both results are stored in a corresponding variable "mean_female" and "mean_male" and printed to user. For the difference between the sexes by age, a new column "Difference (Female - Male)" is added to "df_anal"  which calculates total female minus male and the difference is printed to user.

In part 2 a specific age group is analysed with people within 5 years of a defined age stored in "base_age", in this case 35. Two variables, "younger_group" and "older_group", facilitate the 5 year range calculation around "base_age". The dataframe "df_anal" is filtered to only include rows where "Single Year of Age" falls within the defined range, and the subset is saved in a nwe dataframe "age_group. Female and male populations from "age group" are summed using .sum() and stored into "female_group" and "male_group" variables. The difference between the sexes is then calculated and stored in variable "sexes_diff" and printed to user.

And in part 3 we are required find which irish region has the biggest population difference between sexes in the same age group as part 2. Data fetching and cleansing are similar to part 1, but is this exercise column "Administrative Counties" which contains irsh regions is not dropped from "df". Ireland is also a region in "Administrative Counties" and was removed for the analysis, if kept Ireland would be incorrectly shown as the region with the highest difference for containing the sum of all regions. Age group definitions and variables are the same from part 2.
Finally, to calcutale the difference between regions the script groups the data by "Administrative Counties" using pandas [groupby](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html), summing female and male populations into variables "female_group" and "male_group" using pandas [.agg](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.agg.html), everything is stored into a new Dataframe called "irl_region". A new column "sex_difference" is added into "irl_region" where it calculates the difference between females and males for each region. Using the calculated diference the program identifies the region with the largest sex difference by first identifying the index of the maximum value with pandas [.idxmax()](https://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.DataFrame.idxmax.html) and storing it in variable "region_diff" and pandas ['loc](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html) accesses the specific value for "region_diff" and stores it in "diff_value" variable, the program then prints the results. Fingal is the region with the biggest difference.


#### Assignment 6 - Weather

Part one of this assignment requires to create three plots of Knock’s airport weather data: temperature, mean temperature each day and mean temperature for each month. The libraries imported in this exercise: pandas, matplotlib.pyplot and dates, Seaborn.

First the program reads and imports the data into a dataframe named “df” using the pandas read_csv function where parameter .skiprows is applied to ignore the first 23 rows of unnecessary data from the CSV. Headers and first five lines of data are printed out for user reference. The dates on the Dataframe are stored as strings, pandas .to_datetime converts the data into Datetime with format "%d-%b-%Y %H:%M" (day – month – year – hour – minutes) to ensure dates are standardised.

Plotting the temperature: the function plt.figure  enables control over the plot’s size, in this case defined figsize was (12,5) to obtain a wider plot for better data visualisation. The plot is created using Seaborn .lineplot where the x-axis are the dates and y-axis is the temperature. A title as well as axis labels added using plt.title, plt.xlabel and plt.ylabel and the graph is displayed to using plt.show.

Mean temperature each day plot: the same plt.figure settings from the previous plot are applied and this second graph is also plotted with Seaborn lineplot. Pandas groupby is used in this assignment, it groups the dataframe by date and temperature. Dates are rounded down by date using dt.floor, which ignores time part of Datetime, once the data is grouped, the mean is calculated using .mean().

The mean temperature for each month: to plot the monthly date, the date column is grouped using dt.to_period(“M”) where M tells Python to group the data in months, after that, date and temperature are grouped using .groupby, and the mean is calculated, the result is stored in a variable called “mean_monthly”

When trying execute the plot the following error came up: “argument must be a string or a real number, not 'Period'”, to fix this I used a solution from [Stack Overflow](https://stackoverflow.com/questions/43206554/typeerror-float-argument-must-be-a-string-or-a-number-not-period), converting the index of “mean_monthly” to a timestamp. The monthly mean values were then plotted using plt.plot, as well as title and axis labels.

In Part 2 we are required to plot windspeed data using Python. Plots are from Matplotlib. First some data manipulation is performed. Windspeed is converted to numeric values, all missing data (windspeed = 0) is replaced by NA, to be ignored by Python and do not ...... calculations. The date column is set as a Dataframe index to facilitate slicing, resamplings, etc.
The first plot represents windspeed over time. Data is plotted using matplotlib library, x-axis represent the Dataframe dates and y-axis the windspeed.
The second plot demonstrate the rolling speed over 24 hours using function rolling() and calculating mean.
The third plot shows max windspeed per day, the data is grouped using resample("D"), and max values fetched by max() function.
The forth plot monthly mean of the daily max windspeeds, the daily max previously calculated is grouped by month using resample("ME") and then mean is calculated to the plot.

 
** End **



