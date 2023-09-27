class Solution:
    def reverse(self, x: int) -> int:
        MIN, MAX = -2**31, 2**31 - 1
        res = 0
        if x == 0: return 0
        elif x < 0:
            res = -int(str(-x)[::-1])
        else:
            res = int(str(x)[::-1])
        
        if res < MIN or res > MAX:
            return 0
        
        return res

        