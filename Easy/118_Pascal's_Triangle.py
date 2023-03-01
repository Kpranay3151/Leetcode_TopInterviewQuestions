class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n=numRows
        ans=[]
        if n==1:
            ans.append([1])
            return ans 
        elif n==2:
            ans.append([1])
            ans.append([1,1])
            return ans
        elif n>2:
            ans=[[1],[1,1]]
            for i in range(3,n+1):
                ans.append([])
                c=0
                for j in range(1,i+1):
                    if j==1 or j==i:
                        ans[i-1].append(1)
                    else:
                        r=i-2
                        ans[i-1].append(ans[r][c]+ans[r][c+1])
                        c=c+1
            return ans
    
