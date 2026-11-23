class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        combined = sorted(nums1 + nums2)
        middle = len(combined) // 2
        
        #if there is a remainder 
        if len(combined) % 2 == 1:
            return float(combined[middle])
        
        #no remainder means get middle 2 number and /2
        return float(combined[middle] + combined[middle - 1]) /2



solution = Solution()
nums1 = [1,3]
nums2 = [2]
print(solution.findMedianSortedArrays(nums1,nums2))
