from collections import deque

class Solution:
    def shortestPath(self, mat: list[list[int]]) -> int:
        n, m = len(mat), len(mat[0])

        
        unsafe = [[False] * m for _ in range(n)]
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for r in range(n):
            for c in range(m):
                if mat[r][c] == 0:
                    unsafe[r][c] = True
                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < m:
                            unsafe[nr][nc] = True

        q = deque()

       
        for r in range(n):
            if not unsafe[r][0]:
                q.append((r, 0, 1))
                unsafe[r][0] = True

        while q:
            r, c, dist = q.popleft()

            if c == m - 1:
                return dist

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if (0 <= nr < n and 0 <= nc < m
                        and not unsafe[nr][nc]):
                    unsafe[nr][nc] = True
                    q.append((nr, nc, dist + 1))

        return -1