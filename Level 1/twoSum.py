# Return indices of the two numbers that add up to target.

# Time Complexity: O(n)
# Space Complexity: O(n)
def twoSum(nums, target):
    # Hashmap
    indices = {}

    for i, num in enumerate(nums):
        diff = target - num

        if diff in indices:
            # Solution found
            return [indices[diff], i]
        
        # Update hashmap if no solution
        indices[num] = i
    
def main():
    nums = [2, 7, 11, 15]
    target = 9

    result = twoSum(nums, target)
    print(result)

if __name__ == "__main__":
    main()