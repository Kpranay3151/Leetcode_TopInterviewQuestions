class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=prices
        if p==sorted(p,reverse=True):
            return 0
        ans=[]
        l=0
        r=0
        for i in range(len(p)):
            if i==0:
                l=p[i]
                r=p[i+1]
            if i<len(p)-1 and l<p[i+1]:
                ans.append(p[i+1]-l)
            elif i<len(p)-1 and l>p[i+1] :
                l=p[i+1]
        return max(ans)
