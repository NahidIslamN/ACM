class Solution:
    def isPalindrome(self, x):
        s=str(x)
        if s==s[::-1]:
            return True
        else:
            return False  
x=Solution()
print(x.isPalindrome(-121))
