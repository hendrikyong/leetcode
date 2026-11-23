class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        #helper function to expand around center
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        #loop through the string and expand around each character
        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i + 1)

            #update longest if a longer palindrome is found
            longest = max(longest, odd, even, key=len)
        return longest

solution = Solution()
s = "babad"
print(solution.longestPalindrome(s))