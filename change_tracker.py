#----------Built-in Libraries----------#
from datetime import datetime
import time
import os
import shutil
#----------Built-in Libraries----------#

#----------Third Party Libraries----------#
import datacompy
import pandas as pd
import win32com.client as win32
#----------Third Party Libraries----------#

#----------Project Module----------#
from user_variables import *
#----------Project Module----------#

#----------Class Creation----------#
# This class is created to specify where to download the csv file, what column to join on, how often to run the /
#automation, and how long to keep daily change archives. Modify as needed to fit the user's automation
class ChangeTracker:
    def __init__(self, name, url, compare_col, frequency, archive_length):
        self.name = name
        self.url = url
        self.compare_col = compare_col
        self.frequency = frequency
        self.archive_length = archive_length
    # ----------Class Creation----------#

    #----------Methods----------#
    # This method simply deletes the old file to make room for a new set of comparison files
    def delete_old_file(self):
        os.remove(f"{root_folder}//{self.name} Download - Old.csv")

    # This method changes the new file to old to make room for a brand new file
    def new_file_becomes_old_file(self):
        old_name = f"{root_folder}//{self.name} Download - New.csv"
        new_name = f"{root_folder}//{self.name} Download - Old.csv"
        os.rename(old_name, new_name)

    # This method replaces the new file
    def download_today_file(self):
        df = pd.read_csv(self.url)
        df.to_csv(f"{root_folder}//{self.name} Download - New.csv")

    # This method renames the existing text file in the main folder and places it in the archive folder to make room /
    # for a new text file
    def rename_previous_text_file_and_archive(self):
        os_time_format = os.path.getmtime(f"{root_folder}//{self.name} Download - New.csv")
        mod_date_format = datetime.fromtimestamp(os_time_format).strftime("%Y-%m-%d")
        old_name = f"{root_folder}//{self.name} {self.frequency} Change Tracker.txt"
        new_name = f"{root_folder}//{self.name} {self.frequency} Change Tracker - {mod_date_format}.txt"
        os.rename(old_name, new_name)
        old_location = f"{root_folder}//{self.name} {self.frequency} Change Tracker - {mod_date_format}.txt"
        new_location = f"{root_folder}//Archive of Daily Changes//{self.name} {self.frequency} Change Tracker - {mod_date_format}.txt"
        shutil.move(old_location, new_location)

    # This method uses the datacompy library to compare the two csv files and write to a text file in the root folder
    def compare_dataframes_and_write_text_file(self):
        df1 = pd.read_csv(f"{root_folder}//{self.name} Download - New.csv")
        df2 = pd.read_csv(f"{root_folder}//{self.name} Download - Old.csv")
        comparison = datacompy.Compare(df1, df2, join_columns=self.compare_col, on_index=False, df1_name="Noise Complaints - New", df2_name="Noise Complaints - Old")
        with open(f"{root_folder}//{self.name} {self.frequency} Change Tracker.txt", "w") as f:
            f.write(comparison.report())

    # This method checks the monitor file to see if any changes occurred to items in that list and sends an email /
    # only if there were changes
    def check_monitor_file_and_send_email(self):
        check_list = []
        with open(f"{root_folder}{self.name}//{self.name} {self.frequency} Change Tracker.txt", "w") as f:
            text = f.read()
            for request in monitor_list:
                if request in text:
                    check_list.append("True")
                else:
                    check_list.append("False")
        if "True" in check_list:
            outlook = win32.Dipsatch
            mail = outlook.CreateItem(0)
            mail.To = to_address
            mail.Subject = email_subject
            mail.Body = email_body
            mail.Attachments.Add(f"{root_folder}{self.name}//{self.name} {self.frequency} Change Tracker.txt")

    # This method scans the archive folder and deletes old files depending on how long the user wants to keep them
    def delete_old_archives(self):
        path = f"{root_folder}//Archive of Daily Changes//"
        current_time = time.time()
        days_to_delete = self.archive_length
        for file in os.listdir(path):
            filestamp = os.stat(os.path.join(path, file)).st_mtime
            filecompare = current_time - (days_to_delete * 86400)
            if filestamp < filecompare:
                os.remove(os.path.join(path, file))
    # ----------Methods----------#