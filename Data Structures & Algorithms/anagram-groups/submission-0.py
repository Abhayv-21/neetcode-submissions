class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[""]]

        seen = {}

        for i in strs:
            ch = "".join(sorted(i)) 
            if ch not in seen:
                seen[ch] = [i]
            else:
                seen[ch].append(i)
        
        return list(seen.values())
 