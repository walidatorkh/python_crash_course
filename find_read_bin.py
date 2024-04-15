import os

def find_and_read_bin_files(root_dir):
    bin_files_data = {}
    found_files_count = 0
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.bin'):
                file_path = os.path.join(dirpath, filename)
                with open(file_path, 'rb') as file:
                    bin_files_data[file_path] = file.read()
                found_files_count += 1
    print(f"Found {found_files_count} binary files.")
    print(f"Found {bin_files_data} binary files.")
    return bin_files_data

# Example usage:
root_directory = 'C:\\Automation\\New_folder\\'
bin_files_data = find_and_read_bin_files(root_directory)
for file_path, data in bin_files_data.items():
    print("File:", file_path)
    print("Data:", data)
