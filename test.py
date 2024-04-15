import re

def sum_integers(filename):
    with open(filename, 'r') as file:
        text = file.read()
        numbers = re.findall(r'\b\d+\b', text)
        print(fr'Found numbers : {numbers}')
        return sum(map(int, numbers))

# Example usage:
filename = "C:\\Automation\\New_folder\\test.txt"
total_sum = sum_integers(filename)
if total_sum is not None:
    print("Total sum of integers in the file:", total_sum)