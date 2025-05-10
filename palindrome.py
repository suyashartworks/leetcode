class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        l = len(s)
        i=0
        while i<(l/2):
            if s[i] != s[l-i-1]:
                return False
            else:
                i=i+1
                continue
        return True