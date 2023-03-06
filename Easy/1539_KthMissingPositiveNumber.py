class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        m=[]
        i=1
        while len(m)<=k:
            if i in arr:
                i=i+1
                #print(i)
                pass
            else:
                #print(i)
                m.append(i)
                i=i+1
        return m[k-1]
