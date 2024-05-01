def merge_and_sort_lists(list1: list, list2: list):
    """
    Merges two lists, removes duplicates, and returns a sorted list.

    Args:
        list1 (list): First input list.
        list2 (list): Second input list.

    Returns:
        list: Combined list with unique elements, sorted in ascending order.
    """
    combined_list = list1 + list2
    unique_sorted_list = sorted(set(combined_list))
    return unique_sorted_list


# Example usage:
list1 = [23, 45, 65, 65, 65, 31, 1, 89, 69, 69, 69]
list2 = [67, 89, 23, 45, 8, 65, 65, 90, 69, 69]
result = merge_and_sort_lists(list1, list2)
print("The resultant merged and sorted list is:", result)
