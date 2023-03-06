class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=set(nums1)
        b=set(nums2)
        ans=[]
        c=a.intersection(b)
        c=list(c)
        for i in c:
            t=0
            t=min(nums1.count(i),nums2.count(i))
            for j in range(t-1):
                ans.append(i)
        return c+ans
