import os
import shutil


folderPath= input("Enter The Folder Path to get it sorted")
rules={
    'Images':['jpg','jpeg','png','gif','svg'],
    'Archives':['zip','rar','7z','gz','tar'],
    'Videos':['mp4','mkv','mov','avi'],
    "Audio": ["mp3", "wav", "flac", "aac"],
    'Document':['docx','doc','pdf','pptx','txt','xlsx'],
    "Application":['exe']
}

if not os.path.isdir(folderPath): #Checks is the path given is relevant or not.

    print(f"Error:The path/Folder{folderPath} does not exists!")
    print('Please Enter a Relevant Path')
else:
    print("Starting the Process")

    for filename in os.listdir(folderPath): # here it checks the extensions and based on it starts sorting
        Path = os.path.join(folderPath,filename)
        if os.path.isfile(Path):
            try:
                extension = filename.split('.')[-1].lower()
            except IndexError:
                extension = ''



            destination="other"

            for folder ,extension_list in rules.items():
                if extension in extension_list:
                    destination = folder
                    break


            destination_folder = os.path.join(folderPath, destination)
            if not os.path.exists(destination_folder): # if there is no folder it will create a Seprate folder for the designed file
                os.makedirs(destination_folder)
                print(f"Created new  folder:{destination}")



            shutil.move(Path,destination_folder) # here theh files are moved from the "Other" folder to  its grouped folder
            print(f"Moved '{filename}' to the '{destination}' folder.")


    print("\nSorting Completed")