str1 = "qwerty"
str2 = "ytrewq"

print(f'Print before transformation str1: {str1}')
print(f'Print before transformation str2: {str2}')


def make_equal(str1, str2):
    if len(str1) != len(str2):
        return "The strings must be of the same length"
    else:
        str1 = list(str1)
        str2 = list(str2)
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                str1[i] = str2[i]
        print(f'Print after transformation str1: {str1}')
        return ''.join(str1)


str1_after_transfom = make_equal(str1, str2)
print(f'str1_after_transfomation: {str1_after_transfom}')
