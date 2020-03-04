class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        
        def dfs(board: str, count: dict) -> int:
            if not board:
                return 0
            res, i = float('inf'), 0
            while i < len(board):
                j = i + 1
                while j < len(board) and board[i] == board[j]:
                    j += 1
                need = 3 - (j - i)
                if count[board[i]] >= need:
                    need = 0 if need < 0 else need
                    count[board[i]] -= need
                    new = dfs(board[:i] + board[j:], count)
                    count[board[i]] += need
                    if new >= 0:
                        res = min(res, new + need)
                i = j
            return res if res < float('inf') else -1
        
        return dfs(board, collections.Counter(hand))
