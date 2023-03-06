class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        t1=''
        t2=''
        if len(set(strs))==1:
            return strs[0]
        for i in strs:
            if i=="":
                return ""
            t1=t1+" "+i
            t2=t2+i
        f=" "
        for i in t2:
            f+=i
            if t1.count(f)>=len(strs):
                pass
            else:
                return f[1:-1]
        return f
