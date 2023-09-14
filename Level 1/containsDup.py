# Problem: https://leetcode.com/problems/contains-duplicate/description/
# Description: Return true if any value appears at least twice in the array, else false

# Time Complexity: O(n)
# Space Complexity: O(n)
def containsDuplicate(nums):
    numsHash = {}
    
    for i in nums:
        # Check if i exists in hashMap before we add it
        if i in numsHash:
            return True
        else:
            # If it does not exist, add i
            numsHash[i] = i
    return False

nums = [1,2,3,1]
nums2 = [1,2,3,4]
nums3 = [1,1,1,3,3,4,3,2,4,2]

print(containsDuplicate(nums2))