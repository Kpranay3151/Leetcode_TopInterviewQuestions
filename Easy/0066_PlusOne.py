class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=''
        for i in digits:
            n+=str(i)
        n=str(int(n)+1)
        l=[]
        for i in n:
            l.append(int(i))
        return l
