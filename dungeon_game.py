class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        R, C = len(dungeon), len(dungeon[0])
        dp = [[0] * C for _ in range(R)]
        for i in range(R)[::-1]:
            for j in range(C)[::-1]:
                if i == R - 1 and j == C - 1:
                    dp[i][j] = max(1, 1 - dungeon[i][j])
                elif i == R - 1:
                    dp[i][j] = max(1, dp[i][j + 1] - dungeon[i][j])
                elif j == C - 1:
                    dp[i][j] = max(1, dp[i + 1][j] - dungeon[i][j])
                else:
                    dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j])
        return dp[0][0]
