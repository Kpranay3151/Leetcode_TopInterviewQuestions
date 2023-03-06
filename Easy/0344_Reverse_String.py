class Solution:
    def reverseString(self, s: List[str]) -> None:
        t=''
        n=len(s)
        if n%2==0:
            for i in range(n):
                if i==n//2:
                    break
                else:
                    t=s[i]
                    s[i]=s[n-i-1]
                    s[n-i-1]=t
        else:
            for i in range(n):
                if i==(n//2):
                    break
                else:
                    t=s[i]
                    s[i]=s[n-i-1]
                    s[n-i-1]=t

        
