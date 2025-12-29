class Solution(object):
    def reverse(self, num):
        """
        :type x: int
        :rtype: int
        """
        if num < 0:
            n = -num
            reverse = 0
            while n>0:
                last = n%10
                reverse = reverse*10+last
                n = n//10
            reverse = -reverse
            # return -reverse
            if reverse < -2**31 or reverse > 2**31 - 1:
                return 0
            return reverse
        else:
            reverse = 0
            while num>0:
                last = num%10
                reverse = reverse*10+last
                num = num//10
            # return reverse
            if reverse < -2**31 or reverse > 2**31 - 1:
                return 0
            return reverse