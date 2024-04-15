
from pathlib import Path


def find_files(directory, extension, filenames=None):
    matching_files = []
    count = 0
    p = Path(directory)
    files = p.rglob(f"*{extension}")
    for file in files:
        if filenames and file.name in filenames:
            matching_files.append(file)
            count += 1
        elif not filenames and file.suffix == extension:
            matching_files.append(file)
            count += 1
    return matching_files, count


directory_path = input("Enter directory path: ")
file_extension = input("Enter desired file extension (e.g., '.html', 'YAML', '.txt' etc...): ")
found_files, files_count = find_files(directory_path, file_extension)

print("Found files: ")
for file in found_files:
    print(file)

print(f"Number of files found: {files_count}")
