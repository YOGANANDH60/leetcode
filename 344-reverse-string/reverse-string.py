class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        st = 0
        l = len(s)-1
        while st <= l:
            temp = s[st]
            s[st] = s[l]
            s[l] = temp
            st +=1
            l -=1
        return s