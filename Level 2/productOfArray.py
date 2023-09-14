# Problem: https://leetcode.com/problems/product-of-array-except-self/description/
# Description: Return array[i] such that i equal product of all the elements of nums except nums[i].

# Time Comp: 3 loops, each iterates trough nums once, O(n) + O(n) + O(n) = O(n)
# Space Comp: Same as time comp, 3 lists, O(n) + O(n) + O(n) = O(n)
def productExceptSelf(nums):
    n = len(nums)
    # init arrays with 1s size n
    left = [1] * n
    right = [1] * n
    productArray = [1] * n
    
    # Array for product of left of each element
    for i in range(1, n):
        left[i] = left[i-1] * nums[i-1]
    #print(left)
        
    # Array for product of right of each element
    for i in range(n-2, -1, -1):
        right[i] = right[i+1] * nums[i+1]
    #print(right)

    # Final product
    for i in range(n):
        productArray[i] = left[i] * right[i]
    
    return productArray

nums = [1,2,3,4]
nums2 = [-1,1,0,-3,3]

product = (productExceptSelf(nums))
print(product)