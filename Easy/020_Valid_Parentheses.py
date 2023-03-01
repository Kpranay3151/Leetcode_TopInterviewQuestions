class Solution:
    def isValid(self, s: str) -> bool:
        for i in range(len(s)//2):
            if "()" in s:
                s=s.replace("()","")
            elif "{}" in s:
                s=s.replace("{}","")
            elif "[]" in s:
                s=s.replace("[]","")
        if len(s)<1:
            return True
        else:
            return False
            
