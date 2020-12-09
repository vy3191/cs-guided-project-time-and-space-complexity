"""
Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to the `target`.

Examples:

- two_sum(nums = [2,5,9,13], target = 7) -> [0,1] (nums[0] + nums[1] == 7)
- two_sum(nums = [4,3,5], target = 8) -> [1,2] (nums[1] + nums[2] == 8)

Notes:

- Each input will have only one solution.
- You may not use the same element twice.
- You can return the answer in any order.
"""
def two_sum(nums, target):
    # Your code here
    # for i in range(len(nums)-1):
    #     if nums[i] + nums[i+1] == target: 
    #         return [i, i+1]
    
    num_dict = {}
        
    for i in range(len(nums)):
        num_dict[nums[i]] = i
        
    for i in range(len(nums)):
        # get the current num
        current_num = nums[i]
        #find the complement
        complement = target - current_num
        # check if the compliment is in dict
        if complement in num_dict and i != num_dict[complement]:
            return [i, num_dict[complement]]
        
        
        
print(two_sum(nums=[2,5,9,13], target=7))
print(two_sum(nums = [4,3,5], target = 8))

