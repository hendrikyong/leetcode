class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        #list to return results
        results = []
        for number in nums:
            #square and store in results 
            results.append(number**2)
        #sort the results in ascending 
        results.sort()
        return results 

solution = Solution()
nums = [-4,-1,0,3,10]
print(solution.sortedSquares(nums))
        