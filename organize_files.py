import os
import shutil

def organize_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            extension = filename.split('.')[-1]
            # Add a prefix to avoid conflicts with existing files
            destination_folder = os.path.join(folder_path, f'ext_{extension}')

            # Create the folder if it doesn't exist
            os.makedirs(destination_folder, exist_ok=True)

            # Move the file to the appropriate folder
            shutil.move(file_path, os.path.join(destination_folder, filename))
    print("Files organized by type!")

# Replace with the path to your folder
organize_files('C:\\python\\ext_py')
