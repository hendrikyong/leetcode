class Solution:
    def myAtoi(self, s: str) -> int:
        #strip all leading whitespace
        #criteria 1 
        s = s.lstrip()

        if not s:
            return 0

        #sign and number var 
        sign = 1 
        number = 0

        #criteria 2 
        if s[0] == "-":
            print("num is neg")
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            sign = 1 
            s = s[1:]

        #criteria 3 
        #read s and skip leading 0 or until a non digit char or end of str is reached
        s = s.lstrip("0")
        for i in s:
            if i.isdigit():
                number = number * 10 + int(i)
                print(i)
            else:
                break

        number *= sign 

        #criteria 4 
        if number > 2**31 - 1:
            number = 2**31 - 1
        elif number < -2**31:
            number = -2**31

        return number


solution = Solution()
s = "1337c0d3"
solution.myAtoi(s)