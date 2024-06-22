import os
import time

CURRENT_PROGRAM_NAME = "rename-by-date.py"

def rename_by_date():
    current_directory = os.getcwd()
    files_in_current_directory = os.listdir(current_directory)
    success = False

    for file in files_in_current_directory:
        if file != CURRENT_PROGRAM_NAME:
            file_time = os.path.getctime(file)
            file_time = time.ctime(file_time)

            time_object = time.strptime(file_time)
            time_stamp = time.strftime("%Y-%m-%d %H-%M-%S", time_object)
            time_stamp = time_stamp + ' ' + file

            print("\n" + time_stamp + "\n")
            os.rename(file, time_stamp)
            success = True
    
    if success == True:
            input("\nSuccess! Files were renamed successfully.\n")
            return 0
    else:
        input("No files in current directory.")
        return 1

rename_by_date()