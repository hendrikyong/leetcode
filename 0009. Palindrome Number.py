class Solution:
    def isPalindrome(self, x: int) -> bool:
        #first use %10 to get the last digit
        #then use //10 to get the first few
        number = x
        reversed_number = 0

        while number > 0:
            last_digit = number % 10
            reversed_number = reversed_number * 10 + last_digit
            number = number //10

        if reversed_number == x:
            return True
        else:
            return False 

x = 1221
solution = Solution()
result = solution.isPalindrome(x)

print(result)