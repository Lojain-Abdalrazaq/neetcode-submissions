class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        rows_set = [set() for _ in range(9)]
        columns_set = [set() for _ in range(9)]
        boxes_set = [set() for _ in range(9)]

        for row in range(9):
            for column in range(9):

                number = board[row][column]

                if number == ".":
                    continue

                # box 
                box_no = ( row // 3 ) * 3 + (column // 3)
                if number in rows_set[row]:
                    return False
                if number in columns_set[column]:
                    return False
                if number in boxes_set[box_no]:
                    return False
                
                # not exists, then we add it to the sets:
                rows_set[row].add(number)
                columns_set[column].add(number)
                boxes_set[box_no].add(number)

        return True