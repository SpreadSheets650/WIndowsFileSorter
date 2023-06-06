import os
import shutil

def organize_files(directory):
    files = os.listdir(directory)

    for file in files:
        if os.path.isfile(os.path.join(directory, file)):
            file_extension = os.path.splitext(file)[1]
            target_directory = os.path.join(directory, file_extension[1:].upper() + " Files")

            if not os.path.exists(target_directory):
                os.mkdir(target_directory)

            source_path = os.path.join(directory, file)
            target_path = os.path.join(target_directory, file)

            shutil.move(source_path, target_path)
            print(f"Moved {file} to {target_directory}")

    print("File organization completed!")

def main():
    directory = input("Enter the directory path to organize: ")
    organize_files(directory)

if __name__ == "__main__":
    main()
