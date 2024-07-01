class Solution:
    def lengthOfLongestSubstring(self,s):
        i=0
        j=1
        hel=s[i:j]
        nh=hel
        while j<len(s):
            if s[j] in nh:
                i=i+1
                j=i+1
                nh=s[i:j]
                if len(nh)>=len(hel):
                    hel=nh
                else:
                    pass                
            else:
                j=j+1
                nh=s[i:j]
                if len(nh)>=len(hel):
                    hel=nh
                else:
                    pass
        return len(hel)
x=Solution()
print(x.lengthOfLongestSubstring("suvovesr"))

