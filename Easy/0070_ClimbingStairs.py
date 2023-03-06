class Solution:
    def climbStairs(self, n: int) -> int:
        t=0
        l=[1,2]
        if n==1:
            return 1
        for i in range(2,n):
            t=l[i-2]+l[i-1]
            l.append(t)
        return l.pop()
