import os
import requests
import zipfile
import shutil
import getpass

def download_extract_copy(input_folder, mod_name):
    zip2_url = "https://github.com/fayaz12g/aar-files/raw/main/nss/Layout.zip"
    username = getpass.getuser()
    perm_folder = f"C:/Users/{username}/AppData/Roaming/AnyAspectRatio/perm/nss"
    zip2_file_source = os.path.join(perm_folder, "Layout.zip")
    extract2_folder = os.path.join(input_folder, mod_name, "temp2")
    romfs_folder = os.path.join(input_folder, mod_name, "romfs")
    dst2_folder_path = os.path.join(romfs_folder, "Layout")

    # Ensure the permanent folder exists
    os.makedirs(perm_folder, exist_ok=True)
    
    # Download the ZIP file if it doesn't exist
    if not os.path.isfile(zip2_file_source):
        print("Downloading zip file. This may take up to 10 seconds.")
        response = requests.get(zip2_url)
        with open(zip2_file_source, "wb") as file:
            file.write(response.content)
        print("Zip file downloaded and saved.")

    # Extract the ZIP file
    print(f"Extracting zip to {extract2_folder}. This can also take a few seconds.")
    with zipfile.ZipFile(zip2_file_source, "r") as zip_ref:
        zip_ref.extractall(extract2_folder)

    # Remove existing destination folder if it exists and copy the extracted files
    if os.path.exists(romfs_folder):
        shutil.rmtree(romfs_folder)
    
    os.makedirs(os.path.dirname(dst2_folder_path), exist_ok=True)
    shutil.copytree(extract2_folder, dst2_folder_path)

    # Clean up extracted temporary files
    print("Cleaning up old files")
    shutil.rmtree(extract2_folder)

    print("Process completed successfully.")
