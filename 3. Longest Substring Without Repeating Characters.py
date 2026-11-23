class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        longest = 0
        #loop through s 
        for char in s:
            #check if char in substring
            if char not in substring:
                substring += char
                longest = max(longest, len(substring))
            else:
                substring = substring[substring.index(char) + 1:] + char
        return longest


solution = Solution()
s = "bbbbbbb"
print(solution.lengthOfLongestSubstring(s))