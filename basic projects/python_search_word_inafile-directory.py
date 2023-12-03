import os

def search_number_in_files(directory):
    files_with_number = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                content = file.read()
                num='100'
                if num in content:  
                    files_with_number.append(filename)
    return files_with_number

directory_path = '/home/abdulhakeemk/Desktop/NewFolder'  # Replace this with your directory path
found_files = search_number_in_files(directory_path)

if found_files:
    print("Files containing the number 100:")
    for file_name in found_files:
        print(file_name)
else:
    print("No files containing the number 100 found.")
