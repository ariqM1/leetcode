class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reversed_num = 0
        original_number = x
        while x > 0:
            digit = x % 10
            x = x // 10
            reversed_num = reversed_num * 10 + digit
        
        return original_number == reversed_num
            
