import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ch = re.sub(r'[^a-zA-Z0-9]+', '', s)
        lower = ch.lower()
        return(lower==lower[::-1])
        