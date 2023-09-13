# Convert all uppercase letters into lowercase, removing all non-alphanumeric characters
# If it reads the same forward and backward return True, else False 

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

def main():
    #s = "A man, a plan, a canal: Panama"
    s = "race a car"
    print(isPalindrome(s))

if __name__ == "__main__":
    main()