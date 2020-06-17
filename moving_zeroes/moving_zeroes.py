'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here
    if 0 not in arr:
        return arr

    new_arr = [item for item in arr if item != 0]
    while len(new_arr) < len(arr):
        new_arr.append(0)

    return new_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
