MOD = 10**9 + 7

class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        if not board or not board[0]:
            return [0, 0]
        n = len(board)
        # value grid
        val = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                ch = board[i][j]
                if ch.isdigit():
                    val[i][j] = int(ch)
                elif ch == 'X':
                    val[i][j] = -1  # marker for obstacle
        
        # dp_max[r][c]: max score from (r,c) to (0,0)
        # dp_ways[r][c]: number of ways to achieve it
        INF = float('-inf')
        dp_max = [[INF] * n for _ in range(n)]
        dp_ways = [[0] * n for _ in range(n)]
        
        # base case: E at (0,0)
        if val[0][0] != -1:
            dp_max[0][0] = val[0][0]  # usually 0
            dp_ways[0][0] = 1
        
        directions = [(-1, 0), (0, -1), (-1, -1)]  # up, left, diag
        
        for r in range(n):
            for c in range(n):
                if r == 0 and c == 0:
                    continue
                if val[r][c] == -1:
                    continue  # obstacle
                
                max_from_here = INF
                total_ways = 0
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and dp_max[nr][nc] != INF:
                        candidate = dp_max[nr][nc]
                        if candidate > max_from_here:
                            max_from_here = candidate
                            total_ways = dp_ways[nr][nc]
                        elif candidate == max_from_here:
                            total_ways = (total_ways + dp_ways[nr][nc]) % MOD
                
                if max_from_here != INF:
                    dp_max[r][c] = val[r][c] + max_from_here
                    dp_ways[r][c] = total_ways
                # else remains INF and 0
        
        start_max = dp_max[n-1][n-1]
        if start_max == INF:
            return [0, 0]
        return [start_max, dp_ways[n-1][n-1]]