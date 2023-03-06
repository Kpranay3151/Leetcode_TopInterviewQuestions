class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        l=list(range(97,123))+list(range(48,58))
        for i in s:
            if ord(i) not in l:
                s=s.replace(i,'')
        if s==s[::-1]:
            return True
        else:
            return False
