import re
import requests


def sum_integers(filename: int) -> int:
    with open(filename, 'r') as file:
        text = file.read()
        numbers = re.findall(r'\b\d+\b', text)
        print(fr'Found numbers : {numbers}')
        return sum(map(int, numbers))


# Example usage:
# filename = "C:\\Automation\\New_folder\\test.txt"
# total_sum = sum_integers(filename)
# if total_sum is not None:
#     print("Total sum of integers in the file:", total_sum)


def print_random_joke(substr: str):
    # random = "random"
    url = f"https://api.chucknorris.io/jokes/{substr}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        joke = data["value"]
        print("Random Chuck Norris Joke:")
        print(joke)
    else:
        print("Error fetching random joke. Status code:", response.status_code)
    return substr


random = print_random_joke("random")
# print(random)


def get_random_joke_by_category(substr: str):
    substr = "categories"
    url = f"https://api.chucknorris.io/jokes/{substr}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data)
        return data
    else:
        print("Error fetching random joke. Status code:", response.status_code)
        return None


categories = get_random_joke_by_category("categories")
print(categories)

#
# if __name__ == "__main__":
#     category = "categories"
#     joke = get_random_joke_by_category(category)
#     if joke:
#         print("Random Chuck Norris Joke from category", category + ":")
#         print(joke)
