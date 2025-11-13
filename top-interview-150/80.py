from typing import List

# naive solution
def remove_duplicates_two_naive(nums: List[int]) -> int:
    for num_id in nums:
        while nums.count(num_id) > 2:
            nums.remove(num_id)

    return len(nums)

# O(n) solution
def remove_duplicates_two(nums: List[int]) -> int:
    # Initialize an integer variable i to 0. This variable will keep track of the current position in the modified nums vector.
    current_pos = 0

    # Use a for loop to iterate through each element ele in the nums vector using the range-based for loop.
    for num in nums:
        # i == 0: This condition ensures that the first element is always included in the modified vector.
        # i == 1: This condition ensures that the second element is always included in the modified vector.
        if current_pos == 0 or current_pos == 1:
            nums[current_pos] = num
            current_pos += 1

        # nums[i-2] != ele: This condition checks if the current element ele is not the same as the element two positions before the current position i.
        # This ensures that only two occurrences of any element are included in the modified vector.
        elif nums[current_pos - 2] != num:
            nums[current_pos] = num
            current_pos += 1

    return current_pos



entry = [0,0,1,1,1,1,2,3,3]
print(remove_duplicates_two(entry))
