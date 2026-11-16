class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0

        for number in range(len(s)):
            if number < len(s) - 1:
                if roman[s[number]] < roman[s[number + 1]]:
                    


s = "III"
solution = Solution()
result = solution.romanToInt(s)
print(result)