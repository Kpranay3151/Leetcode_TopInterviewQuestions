class Solution:
    def reverseBits(self, n: int) -> int:
        n=bin(n).replace("0b","")
        s=32-len(n)
        n=s*"0"+n
        n="0b"+n[::-1]
        return int(n,2)
