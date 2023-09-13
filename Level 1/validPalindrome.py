# Problem: https://leetcode.com/problems/valid-palindrome/description/
# Description: Convert string to lowercase & remove non-alphanumeric chars. Return True if Palindrome, else False.

# Time Complexity: O(n)
# Space Complexity: O(n), can improve to O(1) by directly removing all non-alphanumeric characters from s
def isPalindrome(s):
    # Clean string first
    s = s.lower()
    cleanS = ''.join(filter(str.isalnum, s))

    left = 0
    right = len(cleanS)-1
    
    while left < right:
        if cleanS[left] != cleanS[right]:
            return False
        left += 1
        right -=1
    return True

s = "A man, a plan, a canal: Panama"
s2 = "race a car"
print(isPalindrome(s))