import sys
from datetime import datetime

"""
This method will log the text file.
"""


def log_data_process(log_data):
    now=datetime.now()
    currentdattime = now.strftime("%d/%m/%Y %H:%M:%S")
    try: 
        f = open("mylogfile_BankProject.txt", "a")
        f.write(f"{currentdattime} {log_data} \n ")
        f.write(" \n ")
        f.close()
    except:
        print("An exception occurred")