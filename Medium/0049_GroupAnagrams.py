class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l=defaultdict(list)
        for i in strs:
            k=''.join(sorted(i))
            l[k].append(i)
        return l.values()
