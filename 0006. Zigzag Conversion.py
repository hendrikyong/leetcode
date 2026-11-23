class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        current_row = 0
        going_down = False
        rows = ['' for _ in range(numRows)]
        #assign each character to the appropriate row
        for char in s:
            #populate the current row with the character then move down till last row then 
            #change dir and move up till first row then change dir again and repeat
            rows[current_row] += char
            #print(f"Character: {char}, Current Row: {current_row}, Rows: {rows}")
            #this checks if at first or last row then change direction
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down

            #move to the next row
            if going_down:
                current_row += 1
            else:
                current_row -= 1
        
        #print(f"Final Rows: {rows}")
        #combine final rows into a single string
        print(''.join(rows))
        return ''.join(rows)

solution = Solution()
s = "PAYPALISHIRING"
numRows = 3
solution.convert(s, numRows)