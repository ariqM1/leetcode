class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        answer = False
        current = ""

        def backtrack(r, c, index):
            nonlocal answer
            if index == len(word):
                answer = True
                return True
            if r<0 or r>= ROWS or c<0 or c>=COLS:
                return False
            if (r, c) in visited or board[r][c] != word[index]:
                return False

            visited.add((r, c))
            
            backtrack(r+1, c, index+1)
            backtrack(r-1, c, index+1)
            backtrack(r, c+1, index+1)
            backtrack(r, c-1, index+1)
            
            visited.remove((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0):
                    return True
        return answer      