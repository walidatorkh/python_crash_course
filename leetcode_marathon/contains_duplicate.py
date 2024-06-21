from typing import List


def contains_duplicate(self, nums: List[int]) -> bool:
    return len(nums) != len(set(nums))


num1 = [1, 2, 3, 4, 5]
num2 = [1, 2, 3, 3, 2, 1]
print(contains_duplicate(None, num1))
print(contains_duplicate(None, num2))
