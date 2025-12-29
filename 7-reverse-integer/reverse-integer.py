class Solution(object):
    def reverse(self, num):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if num < 0 else 1
        num = abs(num)

        reverse = 0
        while num > 0:
            last = num % 10
            reverse = reverse * 10 + last
            num //= 10

        reverse *= sign

        # 32-bit signed integer check
        if reverse < -2**31 or reverse > 2**31 - 1:
            return 0

        return reverse