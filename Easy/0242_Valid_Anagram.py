class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c=0
        if len(s)!=len(t):
            return False
        else:
            for i in t:
                if i in s and s.count(i)==t.count(i):
                    c=c+1
                else:
                    return False
            if c==len(t):
                return True
            else:
                return False
