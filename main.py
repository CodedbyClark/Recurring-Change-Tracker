# This is the main file for the automation. "change_tracker.py" contains the class creation and all of the methods /
# associated with the class. To run this automation, change the "user_variables.py" to fit your needs and create the /
# class to match the website that you are wanting to track. Please note that this automation only works for websites /
# with a csv download link.

#----------Imports----------#
from change_tracker import *
#----------Imports----------#

#----------Create Object----------#
NoiseComplaints = ChangeTracker(name="NoiseComplaints", url="https://data.montgomerycountymd.gov/api/views/pv7j-pdxw/ro\
ws.csv?accessType=DOWNLOAD", frequency="Daily", compare_col="Case Number", archive_length=30)
#----------Create Object----------#

#----------Run Functions----------#
NoiseComplaints.delete_old_file()
NoiseComplaints.new_file_becomes_old_file()
NoiseComplaints.download_today_file()
NoiseComplaints.rename_previous_text_file_and_archive()
NoiseComplaints.compare_dataframes_and_write_text_file()
NoiseComplaints.check_monitor_file_and_send_email()
NoiseComplaints.delete_old_archives()
#----------Run Functions----------#