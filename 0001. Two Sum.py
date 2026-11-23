class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for number in range(len(nums)):
            remainder = target - nums[number]

            if remainder in seen:
                return [seen[remainder], number]
            
            seen[nums[number]] = number