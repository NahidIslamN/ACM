
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Sort the strings to compare the prefixes of the first and last strings
        strs.sort()
        
        # Compare the first and last strings
        first = strs[0]
        last = strs[-1]
        
        # Find the common prefix between the first and last strings
        for i in range(len(first)):
            if first[i] != last[i]:
                return first[:i]
        
        return first
        
