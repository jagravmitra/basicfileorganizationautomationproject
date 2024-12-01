import os  # Import the os module to interact with the operating system
import shutil  # Import shutil module to move files between directories

# Function to organize files in a specified directory
def organize_files(directory):
    # Define file categories and their corresponding extensions
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
        "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
        "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"]
    }

    # Create folders for each file type if they don't already exist
    for folder in file_types:
        # Create the full path for the folder
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):  # Check if the folder exists
            os.makedirs(folder_path)  # Create the folder if it doesn't exist

    # Iterate through all the files in the specified directory
    for filename in os.listdir(directory):
        # Create the full path to the file
        file_path = os.path.join(directory, filename)

        # Check if the current path is a file (not a folder)
        if os.path.isfile(file_path):
            moved = False  # Flag to check if the file was moved

            # Check the file's extension against the defined categories
            for folder, extensions in file_types.items():
                # If the file's extension matches a category, move the file
                if any(filename.lower().endswith(ext) for ext in extensions):
                    # Define the destination path for the file
                    destination = os.path.join(directory, folder, filename)
                    shutil.move(file_path, destination)  # Move the file
                    print(f"Moved: {filename} to {folder}")  # Log the action
                    moved = True  # Mark the file as moved
                    break  # Exit the loop after moving the file

            # If the file didn't match any category, move it to "Others"
            if not moved:
                # Define the path for the "Others" folder
                other_folder = os.path.join(directory, "Others")
                if not os.path.exists(other_folder):  # Create folder if missing
                    os.makedirs(other_folder)
                shutil.move(file_path, os.path.join(other_folder, filename))  # Move file to "Others"
                print(f"Moved: {filename} to Others")  # Log the action

# Main entry point for the script
if __name__ == "__main__":
    # Ask the user to input the directory path to organize
    directory = input("Enter the path to the directory to organize: ").strip()  # Remove extra whitespace
    directory = os.path.abspath(directory)  # Convert to an absolute path
    if os.path.exists(directory) and os.path.isdir(directory):  # Check if the directory exists and is valid
        organize_files(directory)  # Call the organize_files function
    else:
        # Show an error if the specified directory doesn't exist
        print(f"Error: The directory '{directory}' does not exist or is not a valid directory.")
