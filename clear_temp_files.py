import os
import time

# Function to clear temporary files older than a certain age
def clear_temp_files(folder_path, days_old=7):
    # Get the current time
    now = time.time()

    # Loop through each file in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            # Get the last modified time of the file
            file_age = now - os.path.getmtime(file_path)

            # If the file is older than the specified number of days, delete it
            if file_age > days_old * 86400:  # 86400 seconds = 1 day
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")
    
    print("Temporary files cleaned!")

# Specify the folder path for temporary files
# Example: C:\Users\Sweety\AppData\Local\Temp or any other folder
folder_to_clean = r'C:\Users\Sweety\AppData\Local\Temp'

# Call the function to clean the temp files (change the folder path if necessary)
clear_temp_files(folder_to_clean)
