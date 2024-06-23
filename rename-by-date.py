import os
import time

CURRENT_PROGRAM_NAME = "rename-by-date.py"

# main function
def rename_by_date():
    # initialize variables
    current_directory = os.getcwd()
    files_in_current_directory = os.listdir(current_directory)
    success = False

    time_user_choice = ''
    while True:
        time_user_choice = input('\nChoose the time: C - creation, M - modification, E - exit\n').upper()
        if time_user_choice in ['E']:
            return 0
        elif time_user_choice in ['C', 'M']:
            break

    folder_user_choice = ''
    while True:
        folder_user_choice = input('\nRename folders? Y/N\n').upper()
        if folder_user_choice in ['E']:
            return 0
        elif folder_user_choice in ['Y', 'N']:
            break

    # for every filename in the selected files
    for file in files_in_current_directory:
        folder_check = True

        if folder_user_choice == 'N':
            if os.path.isdir(file):
                folder_check = False

        if file != CURRENT_PROGRAM_NAME and folder_check:
            # get the time
            if time_user_choice == 'C':
                file_time = os.path.getctime(file)
            elif time_user_choice == 'M':
                file_time = os.path.getmtime(file)
            file_time = time.ctime(file_time)

            # modify the time into an time object and format it to year-month-day hour-minute-second + it's current name
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
        input("\nNo files in current directory.\n")
        return 1

rename_by_date()