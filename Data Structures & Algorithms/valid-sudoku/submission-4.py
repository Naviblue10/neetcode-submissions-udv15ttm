class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for _ in range(9)]
        columns=[set() for _ in range(9)]
        blocks=[set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val=board[i][j]

                if val =='.':
                        continue
                block_indx=(i//3) * 3 + (j//3)
                if(val in rows[i]) or (val in columns[j]) or (val in blocks[block_indx]):
                        return False
                
                rows[i].add(val)
                columns[j].add(val)
                blocks[block_indx].add(val)

        return True
