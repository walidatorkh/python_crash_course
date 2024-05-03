def bizz_bazz():
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
