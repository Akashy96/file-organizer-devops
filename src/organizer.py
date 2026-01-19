import os
import shutil

FILES_MAP = {
    "images": [".jpg", ".jpeg", ".png", ".gif"],
    "documents": [".pdf", ".docx", ".txt"],
    "spreadsheets": [".xls", ".xlsx", ".csv"],
}

def organize_files(path):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):
            moved = False

            for folder, extensions in FILES_MAP.items():
                if file.lower().endswith(tuple(extensions)):
                    folder_path = os.path.join(path, folder)
                    os.makedirs(folder_path, exist_ok=True)

                    destination = os.path.join(folder_path, file)

                    if not os.path.exists(destination):
                        shutil.move(file_path, destination)

                    moved = True
                    break

            if not moved:
                other_path = os.path.join(path, "others")
                os.makedirs(other_path, exist_ok=True)

                destination = os.path.join(other_path, file)

                if not os.path.exists(destination):
                    shutil.move(file_path, destination)

if __name__ == "__main__":
    organize_files(".")