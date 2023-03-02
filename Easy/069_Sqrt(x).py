class Solution:
    def mySqrt(self, x: int) -> int:
        t=0
        i=1
        while x>0:
            x=x-i
            i=i+2
            t=t+1
        if x==0:
            return t
        else:
            return t-1
        
