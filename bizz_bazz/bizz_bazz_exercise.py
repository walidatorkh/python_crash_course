def bizz_bazz():
    """
    Generate a list of numbers from 1 to 50, replacing multiples of 3 with "bizz !!!",
    multiples of 5 with "bazz!!!", and multiples of both 3 and 5 with "BIZZ & BAZZ".

    Returns:
        str: A string containing the generated list separated by newline characters.
    """
    sorted_list = list(range(1, 51))
    result = []
    for number in sorted_list:
        if number % 3 == 0 and number % 5 == 0:
            result.append("BIZZ & BAZZ")
        elif number % 3 == 0:
            result.append("bizz !!!")
        elif number % 5 == 0:
            result.append("bazz!!!")
        else:
            result.append(str(number))
    return '\n'.join(result)


print(bizz_bazz())
