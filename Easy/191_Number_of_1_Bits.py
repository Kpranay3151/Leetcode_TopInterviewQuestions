class Solution:
    def hammingWeight(self, n: int) -> int:
        t=bin(n)
        return t.count("1")
