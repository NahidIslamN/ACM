class Solution:
    def rotate(self, List, k):
        while k>0:
            x = List.pop()
            List.insert(0,x)
            k = k-1
        return List


# Test
x = Solution()
print(x.rotate(List=[10,20,60],k=3))
