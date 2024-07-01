class Solution:
    def relativeSortArray(self, arr1, arr2):
        temp_arry=[]
        result_arry = []
        for x in arr2:
            for y in arr1:
                if x == y :
                    result_arry.append(y)
        for z in arr1:
            if z in result_arry:
                pass
            else:
                temp_arry.append(z)
                
        temp_arry.sort()
        result_arry=result_arry + temp_arry        
        return result_arry

arr1=[20,30,10,22,1,1,2,1,2,52,14,1]
arr2=[1,2,20]
obj = Solution()
print(obj.relativeSortArray(arr1,arr2))

