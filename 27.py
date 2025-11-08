from typing import List

def remove_element(nums: List[int], val: int) -> int: 
    for num_idx in range(len(nums)):
        if nums[num_idx] == val:
            nums[num_idx] = "_"
    
    nums[:] = [num for num in nums if num != "_"]
    return len(nums)