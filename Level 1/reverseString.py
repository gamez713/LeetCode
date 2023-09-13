# Reverse regular string practice

def reverse(s):
    rev_string = ""
    n = len(s)

    for i in range(n):
        rev_string += s[n-i-1]

    return rev_string
    
def main():
    string = "Hello World"

    reverseString = reverse(string)
    print(reverseString)

if __name__ == "__main__":
    main()