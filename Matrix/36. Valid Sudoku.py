class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        sub_boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                
                # Determine the index of the sub-box
                sub_box_index = (i // 3) * 3 + (j // 3)
                
                if num in rows[i] or num in columns[j] or num in sub_boxes[sub_box_index]:
                    return False
                
                rows[i].add(num)
                columns[j].add(num)
                sub_boxes[sub_box_index].add(num)
        
        return True
