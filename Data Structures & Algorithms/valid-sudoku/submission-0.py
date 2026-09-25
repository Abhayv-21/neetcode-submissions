class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if len(board) == 0:
            return True

        for i in range(9):
            seen = set()

            for j in range(9):
                num = board[i][j]

                if num == ".":
                    continue

                if "1" > num  or num > "9":
                    return False 

                if num in seen:
                    return False

                seen.add(num)

        for j in range(9):
            seen1 = set()

            for i in range(9):
                num = board[i][j]

                if num == ".":
                    continue
                
                if "1">num or num>"9":
                    return False

                if num in seen1:
                    return False
                seen1.add(num)

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                seen2 = set()

                for i in range(row, row+3):
                    for j in range(col, col+3):
                        num = board[i][j]
                        if num == ".":
                            continue
                        if num in seen2:
                            return False
                        seen2.add(num) 

        return True
