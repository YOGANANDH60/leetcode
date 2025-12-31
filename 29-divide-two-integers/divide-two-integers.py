class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        m = int(dividend /divisor)
        
        if m < -2**31 or m > 2**31 - 1:
                return m-1
        return m