import os  
import shutil  

# Define the directory to organize (Desktop)
directory = os.path.join(os.path.expanduser("~"), "Desktop")


extensions = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Audio": [".mp3", ".wav"],
    "Video": [".mp4", ".mov"],
}


for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)  

    if os.path.isfile(file_path):  
        file_extension = os.path.splitext(filename)[1].lower()  
        moved = False  

       
        for category, ext_list in extensions.items():
            if file_extension in ext_list:  
                folder_name = category  #
                folder_path = os.path.join(directory, folder_name)  
                os.makedirs(folder_path, exist_ok=True) 
                shutil.move(file_path, os.path.join(folder_path, filename))  
                print(f"Moved {filename} to {folder_name} folder.")
                moved = True  
                break  

        if not moved: 
            others_path = os.path.join(directory, "Others")
            os.makedirs(others_path, exist_ok=True)
            shutil.move(file_path, os.path.join(others_path, filename))
            print(f"Moved {filename} to Others folder.")
    else:
        print(f"Skipped {filename}. It is a directory.")

print("File organization completed.")
