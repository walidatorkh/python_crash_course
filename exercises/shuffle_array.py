import random


def shuffle_array(arr):
    shuffled_arr = arr[:]  # Create a copy of the array to avoid modifying the original
    n = len(shuffled_arr)
    '''
        Fisher-Yates shuffle algorithm
        For an array of n elements, it starts from the last element and goes to the first. 
        At each step, it selects a random element from the already traversed part of the array 
        (that is, among the elements that have not yet been moved) 
        and swaps it with the current element.
    '''
    for i in range(n - 1, 0, -1):
        # Choose a random index between 0 and i
        j = random.randint(0, i)
        # Swap elements at indices i and j
        shuffled_arr[i], shuffled_arr[j] = shuffled_arr[j], shuffled_arr[i]
    return shuffled_arr


# Example usage
input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
shuffled_array = shuffle_array(input_array)
print("Original array:", input_array)
print("Shuffled array:", shuffled_array)
