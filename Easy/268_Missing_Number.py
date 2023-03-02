class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        f=(n*(n+1))//2
        if f==sum(nums):
            return 0
        else:
            return f-sum(nums)
