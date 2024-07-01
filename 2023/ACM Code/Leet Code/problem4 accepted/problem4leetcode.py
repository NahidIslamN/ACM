class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        i=0
        j=0
        k=0
        result=[]
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                result.insert(k,nums1[i])
                i=i+1
                k=k+1
            else:
                result.insert(k,nums2[j])
                j=j+1
                k=k+1
        while i<len(nums1):
                result.insert(k,nums1[i])
                i=i+1
                k=k+1
        while j<len(nums2):
                result.insert(k,nums2[j])
                j=j+1
                k=k+1
        x=len(result)
        if x%2==0:
            mid_ind=(x-1)//2
            final_result=format((result[mid_ind]+result[mid_ind+1])/2,".5f")  
        else:
            mid_ind=(x)//2
            final_result= format(result[mid_ind],".5f")
        return float(final_result)
