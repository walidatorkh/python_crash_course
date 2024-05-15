import random


# digits = list(range(100))
# random.shuffle(digits)
def calculate(s: str) -> int:
    length = len(s)

    if length > 100:
        return 0

    count = [0] * 100
    for i in range(length - 1):
        num = int(s[i: i + 2])
        # print(num)
        count[num] = 1
    # print(num)
    return sum(count)


def solution() -> str:
    result = []
    for i in range(100):
        result.append(f"{i:02}")

    # Convert list to string
    output = "".join(result)

    #  Restrict for 100 characters in output
    print(f"output: {output}")
    return output[:100]


# Example usage:
generated_string = solution()
print("Generated String:", generated_string)
print("Calculate Result:", calculate(generated_string))
