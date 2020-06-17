'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    # x and y defines the lower(left) and upper(right) bound of the window at any point
    x = 0
    y = k
    maximums = []

    while y <= len(nums):
        window = nums[x:y]
        max_in_window = max(window)
        maximums.append(max_in_window)

        x += 1
        y += 1

    return maximums


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    # [1,3,-1,-3,5,3,6,7]
    # [3,3,5,5,6,7]
    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
