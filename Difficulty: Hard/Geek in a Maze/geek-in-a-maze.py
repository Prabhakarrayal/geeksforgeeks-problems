from collections import deque

class Solution:
    def numberOfCells(self, r: int, c: int, u: int, d: int, mat: list[list[int]]) -> int:
        n = len(mat)
        m = len(mat[0])

        if mat[r][c] == '#':
            return 0

        INF = 10**9

        
        dist = [INF] * (n * m)

        start = r * m + c
        dist[start] = 0

        dq = deque([start])

        while dq:
            cur = dq.popleft()

            x = cur // m
            y = cur - x * m
            cur_dist = dist[cur]

            # Up
            if x > 0 and mat[x - 1][y] != '#':
                nxt = cur - m

                if cur_dist + 1 < dist[nxt]:
                    dist[nxt] = cur_dist + 1
                    dq.append(nxt)

            
            if x + 1 < n and mat[x + 1][y] != '#':
                nxt = cur + m

                if cur_dist < dist[nxt]:
                    dist[nxt] = cur_dist
                    dq.appendleft(nxt)

            
            if y > 0 and mat[x][y - 1] != '#':
                nxt = cur - 1

                if cur_dist < dist[nxt]:
                    dist[nxt] = cur_dist
                    dq.appendleft(nxt)

            
            if y + 1 < m and mat[x][y + 1] != '#':
                nxt = cur + 1

                if cur_dist < dist[nxt]:
                    dist[nxt] = cur_dist
                    dq.appendleft(nxt)

        ans = 0

        for i in range(n):
            for j in range(m):
                idx = i * m + j

                if dist[idx] == INF:
                    continue

                up = dist[idx]
                down = up + i - r

                if up <= u and down <= d:
                    ans += 1

        return ans