class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        l=list(range(65,91))
        a=0
        t=0
        for i in columnTitle:
            a=a+((l.index(ord(i))+1)*(26**(len(columnTitle)-t-1)))
            t=t+1
        return a
