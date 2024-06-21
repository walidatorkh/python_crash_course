def is_palindrome_int(x: int) -> bool:
    if x < 0:
        return False

    new = 0
    original = x
    while x:
        x, d = divmod(x, 10)
        new = new * 10 + d
    return new == original


# Convert x to string if it's an integer
# in case need to convert int to string
#     if isinstance(x, int):
#         x = str(x)
def is_palindrome_string(s: str) -> bool:
    normalized_s = s.lower()
    normalized_s = ''.join(filter(str.isalnum, normalized_s))
    return normalized_s == normalized_s[::-1]


num1 = 12345
num2 = 123321
print(is_palindrome_int(num1))
print(is_palindrome_int(num2))

# Примеры использования
print(is_palindrome_string("A man, a plan, a canal: Panama"))  # True, потому что строка читается одинаково с обеих сторон
print(is_palindrome_string("race a car"))  # False, потому что строка не читается одинаково с обеих сторон
print(is_palindrome_string("level"))  # True, потому что "level" читается одинаково с обеих сторон
