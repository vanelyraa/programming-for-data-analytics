# programming-for-data-analytics-assessment

# Programming for Data Analytics Assessment

## Table of Contents
 - [Project Purpose](#project-purpose)
 - [Setup Instructions](#setup-instructions)
 - [Install Dependencies](#install-dependencies)
 - [Project Results](#project-results)

## Project Purpose
This repository contains my project submissions for the Programming for Data Analytics module completed as part of the Higher Diploma in Science in Computing in Data Analytics at ATU.

## Install Dependencies
All required libraries are listed in requirements.txt  

## Setup Instructions
Clone this GitHub repository:
<pre> git clone https://github.com/vanelyraa/programming-for-data-analytics.git </pre>

Navigate the project directory:
<pre> cd programming-for-data-analytics/project </pre>

Create a virtual environment (optional):
<pre> python3 -m venv venv </pre>

Activate virtual environment (optional):  
For windows: <pre> source venv/bin/activate </pre> 
For MacOS: <pre> source venv/bin/activate  </pre> 

Install required dependencies:
<pre> pip install -r requirements.txt </pre>

## Project Results 
In this project I've analysed wind speed across four Irish locations stations close to wind farms - Mace Head, Malin Head, Ireland West Knock Airport, and Gurteen. Two sites were dropped in the early stages of the analysis - Ballyhaise and Mount Dillon as their average wind speed was too close to cut-in average. 

To assess each location's suitability, several analysis were performed such as: hourly, monthly, yearly and seasonal patterns as well as operational and downtime frequency.

Mace Head and Malin Head show the strongest and most consistent wind resources, presenting high mean wind speeds and wind power potential.
Knock Airport presents moderate yet stable patterns, suitable for smaller wind farms.
Gurteen has the lowest wind speed numbers of all sites.

Winter is the season with the strongest winds across all sites and Summer has the weakest wind patterns. Coastal sites (Malin and Mace) have stronger and more reliable winds than inland areas and present the best potential energy production. Inland locations (Knock and Gurteen) show lower wind speeds and are not as reliable for energy production, with higher downtime periods (when winds are too low or too high for turbine operation). 

Overall, the most suitable sites for Wind farms in this study are Mace Head and Malin Head, Knock Airport is moderately suitable, better for small scale Wind farms and Gurteen is the least suitable requiring a specific type of turbine for energy production potential maximisation.