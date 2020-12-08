"""
Demonstration #2

Given a non-empty array of integers `nums`, every element appears twice except except for one. Write a function that finds the element that only appears once.

Examples:

- single_number([3,3,2]) -> 2
- single_number([5,2,3,2,3]) -> 5
- single_number([10]) -> 10
"""
def single_number(nums):
    # Your code here
    for i in range(len(nums)-1):
        if arr[i] == arr[i+1]: 
            return [i, i+1]
        
print(single_number(nums=[2,5,9,13], target=7))
