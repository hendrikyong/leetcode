class Solution:
    def reverseString(self, s: list[str]) -> None:
        left_idx = 0
        right_idx = len(s)-1
        for i in range (len(s) // 2):
            s[left_idx], s[right_idx] = s[right_idx], s[left_idx]
            left_idx +=1
            right_idx -=1

solution = Solution()
s = ["h","e","l","l","o"]
print(solution.reverseString(s))
        