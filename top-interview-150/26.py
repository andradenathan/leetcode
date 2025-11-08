from typing import List

def remove_duplicates(nums: List[int]) -> int:     
    should_replace = []
    
    for nums_id in range(1, len(nums)):
        num = nums[nums_id]
        if nums[nums_id - 1] == num:
            should_replace.append(nums_id)
    
    for replace_id in range(len(should_replace)):
        should_replace_nums_id = should_replace[replace_id]
        nums[should_replace_nums_id] = "_"


    nums[:] = [num for num in nums if num != "_"]
    return len(nums)