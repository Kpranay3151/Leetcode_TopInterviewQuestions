class Solution:
    def isHappy(self, n: int) -> bool:
        def sumd(n):
            t=list(str(n))
            s=0
            for i in t:
                s+=int(i)**2
            return s
        while True:
            n=sumd(n)
            if n==1 or n==7:
                return True
            elif n<10:
                return False

            
