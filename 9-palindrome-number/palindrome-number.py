class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        n = x
        rev = 0

        while x>0:
            last = x %10
            rev = rev*10 +last
            x = x//10
        if n == rev:
            return True
        else:
            return False 