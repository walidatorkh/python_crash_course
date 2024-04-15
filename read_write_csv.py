import csv
import heapq

# Example of employees records
employee_records = [
    {"Full Name": "Vasya Vasilev", "Title": "Manager", "Phone Number": "+972 52-425-0208", "Salary": 50000},
    {"Full Name": "Haim Shvili", "Title": "Developer", "Phone Number": "+972 50-790-3366", "Salary": 75000},
    {"Full Name": "Gogi Petrov", "Title": "QA", "Phone Number": "+972 50-439-9712", "Salary": 35000},
    {"Full Name": "Sara Andersen", "Title": "Product Manager", "Phone Number": "+972 54-469-9699", "Salary": 4000},
    {"Full Name": "Edita Vestering", "Title": "Product Owner", "Phone Number": "+972 54-469-9699", "Salary": 77000},
    {"Full Name": "Roberto Vega", "Title": "QA Automation", "Phone Number": "+972 54-469-9699", "Salary": 88000},
    {"Full Name": "Rudi Droste", "Title": "CEO", "Phone Number": "+972 50-203-0658", "Salary": 9000},
    {"Full Name": "Carolina Lima", "Title": "VP", "Phone Number": "+972 52-848-9626", "Salary": 13000},
    {"Full Name": "Emre Asikoglu", "Title": "HR Partner", "Phone Number": "+972 54-262-5308", "Salary": 15000},
    {"Full Name": "Evan Carlson", "Title": "Developer", "Phone Number": "+1 (347) 243-0208", "Salary": 45500},
    {"Full Name": "Friedrich-Karl Brand", "Title": "Senior Developer", "Phone Number": "+7 952 962-11-99",
     "Salary": 75000},
]

# file CSV naming
csv_filename = "C:\\Automation\\python_crash_course\\employees.csv"
output_csv_file = "C:\\Automation\\python_crash_course\\employees_updated.csv"
# create a CSV file
with open(csv_filename, mode="w", newline="") as file:
    fieldnames = ["Full Name", "Title", "Phone Number", "Salary"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(employee_records)

print(f"File {csv_filename} successfully created.")


def top_10_highest_salaries(csv_file):
    """

    :type csv_file: object
    """
    with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        next(reader)  # missing header

        salaries = []

        for row in reader:
            full_name, title, phone_number, salary = row
            salary = float(salary)

            heapq.heappush(salaries, (salary, full_name))

            if len(salaries) > 10:
                heapq.heappop(salaries)
    file.close()
    return sorted(salaries, reverse=True)


def top_10_lowest_salaries(csv_file, output_csv_file):
    with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        next(reader)  # missing header

        salaries = []

        for row in reader:
            full_name, title, phone_number, salary = row
            salary = float(salary) + 1000

            heapq.heappush(salaries, (salary, full_name))

            if len(salaries) > 10:
                heapq.heappop(salaries)
    file.close()
    with open(output_csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Full Name', 'Title', 'Phone Number', 'Salary'])

        for salary, full_name in sorted(salaries, reverse=False):
            writer.writerow([full_name, title, phone_number, salary])
    file.close()
    return sorted(salaries, reverse=False)



# using example
top_10 = top_10_highest_salaries(csv_filename)
for salary, full_name in top_10:
    print(f"{full_name}: ${salary}")
    print(f"top_10 ########################################")
bottom_top = top_10_lowest_salaries(csv_filename, output_csv_file)
for salary, full_name in bottom_top:
    print(f"{full_name}: ${salary}")
    print(f"top_10 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
