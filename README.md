# <Recurring-Change-Tracker>

## Description
This automation was created to show a simple way of tracking daily changes to a csv file that is commonly updated on a website. The way that I use
the automation is to donwload the csv file everyday at 6:00 AM to a specified folder. The csv file from that day replaces the older csv file in the 
folder and the one from the preious day becomes "yesterday". Below is an example of the steps:
- Delete yesterday csv file
- Today csv file becomes the new yesterday csv file
- Download a new today csv file

At this point in the process, the automation uses the "datacompy" external library which is a pre-formatted text file output that compares two csv files. 
The user can either use the pre-formatted file that it creates or modify the text with a few additional lines of code. That .txt file output is then saved
in that same folder, and the .txt file from the day before goes into the archive folder for a specified amount of days. The last part of the automation checks to see if there are any important changes in the "monitor_list" global variable input file and then sends an email to the user as needed. 

- This project is very beneficial for anyone who is trying to track daily changes to a csv file attachment on a website. 
- I built this project, because I was constantly using "vlookup" in excel to see what changes had been made to a file at work. This project provides 
an organized tracking system for daily changes being made to a csv file. 
- I learned a lot about pandas and file directory management in Python by creating this project.

## Installation
To run this automation, the user just needs to create a .bat file pointing to the "main.py" file and to a Python executable. To personalize the project
for the user's need, you will need to change the "user_variables.py" file in a text editor to specify the following:
- Root folder to save the project output 
- Subject of the email automation
- Message body of the email automation
- The email address of where the email automation goes
- A monitor list to specify if the text file contains changes to these "ids" or anything else that it will send the email. If this is not specified, an 
email will never be sent

The last item the user will need to specify is the "main.py" file. The only thing that needs to be changed in this file is the "Create Object" portion. 
The user will need to create a new object with attributes that match the needs of the website to track. The example in the automation is a "noise complaint" csv file that is updated constantly.
