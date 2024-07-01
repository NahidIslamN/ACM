class Solution:
    def myAtoi(self,s):
        i=0
        final_result=""
        result=""
        while i<len(s):
            if 48<=ord(s[i])<=57 or 45==ord(s[i]):
                result=result+s[i]
                if len(result)<final_result:
                    pass
                else:
                    final_result=result
                i=i+1
            elif ord(s[i])==32:
                i=i+1
            else:
                i=i+1
        return int(result)
x=Solution()
print(x.myAtoi("975 with owrd"))
#print(ord(" "))



