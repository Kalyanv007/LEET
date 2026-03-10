class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def is_palindrome(string):
            return string == string[::-1]
        
        for i in range(len(s),0,-1):
            prefix=s[:i]
            if is_palindrome(prefix):
                suffix=s[i:]
                return suffix[::-1]+s
        return s