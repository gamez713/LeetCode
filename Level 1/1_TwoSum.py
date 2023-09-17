# Problem: https://leetcode.com/problems/two-sum/description/
# Description: Return indices of the two numbers that add up to target.

# Time Complexity: O(n)
# Space Complexity: O(n)
def twoSum(nums, target):
    # Create Hashmap
    indices = {}

    for i, num in enumerate(nums):
        diff = target - num

        if diff in indices:
            # Solution found
            return [indices[diff], i]
        
        # Update hashmap if no solution
        indices[num] = i

nums = [2, 7, 11, 15]
target = 9

result = twoSum(nums, target)
print(result)