class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def expand(l, r):
            res = ""
            resLen = 0
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                l -= 1
                r += 1

            return s[l+1: r]
        
        longest = ""
        for i in range(n):
            l, r = i, i
            odd_palindrome = expand(l, r)
            even_palindrome = expand(l, r+1)

            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
        
            if len(even_palindrome) > len(longest):
                longest = even_palindrome
        
        return longest
                 