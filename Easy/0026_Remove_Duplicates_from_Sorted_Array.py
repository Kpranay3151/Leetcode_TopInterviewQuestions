class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        t=sorted(list(set(nums)))
        for i in range(len(t)):
            nums[i]=t[i]
        return len(t)
