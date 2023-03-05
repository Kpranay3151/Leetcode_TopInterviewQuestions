class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<1:
            return False
        if n==1:
            return True
        while True:
            if n%3==0:
                n=n/3
            else:
                return False
            if n==1:
                return True
