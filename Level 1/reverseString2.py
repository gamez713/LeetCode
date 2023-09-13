# Reverses a string (input string is given as an array of characters)

# Time Complexity: O(n)
# Space Complexity: O(n)
def reverseString(s):
    rev_string = []
    n = len(s)

    for i in range(n):
        rev_string.append(s[n-i-1])

    for i in range(n):
        s[i] = rev_string[i]

    return(s)

# Time Complexity: O(n)
# Space Complexity: O(1)
def O1_solution(s):
    left = 0
    right = len(s)-1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return(s)

def main():
    s = ["h","e","l","l","o"]
    s2 = ["H","a","n","n","a","h"]

    rev = reverseString(s)
    print(rev)

    revO1 = O1_solution(s2)
    print(revO1)

if __name__ == "__main__":
    main()