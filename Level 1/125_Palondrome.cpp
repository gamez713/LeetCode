// Problem: https://leetcode.com/problems/valid-palindrome/description/
// Description: Convert string to lowercase & remove non-alphanumeric chars. Return True if Palindrome, else False.
#include <iostream>
#include <algorithm>
#include <cctype>

using namespace std;

string formatString(string text) {
    transform(text.begin(), text.end(), text.begin(), ::tolower);
    string result;

    for (int i = 0; i < text.size(); i++) {
        if (isalnum(text[i])) { 
            result += text[i];
        }
    }

    return result;
}

bool isPalindrome(string s) {
    string text = formatString(s);
    int n = text.length();

    int left = 0;
    int right = n - 1;

    while (left < right) {
        if (text[left] != text[right]) {
            return false;
        }
        left++;
        right--;
    }

    return true;
}

int main() {
    string s = "A man, a plan, a canal: Panama";
    cout << isPalindrome(s) << endl;

    string s2 = "race a car";
    cout << isPalindrome(s2) << endl;

    string s3 = " ";
    cout << isPalindrome(s3) << endl;

    return 0;
}