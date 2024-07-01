class Solution:
    def twoSum(self,List, target):
        for x in range(len(List)-1,0,-1):
            for i in range(x):
                if List[x]+List[i]==target:
                    result=[i,x]
                    break
                elif List[i]+List[i+1]==target:
                    result=[i,i+1]
                    break
        return result

obj=Solution()
x=obj.twoSum(List=[-3,4,3,90],target=7)
print(x)
