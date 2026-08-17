from collections import deque

class Solution:
    def minThrows(self, n, lad, sn):
        N = n * n

        jump = [-1] * (N + 1)

        # Ladders
        for i in range(0, len(lad), 2):
            jump[lad[i]] = lad[i + 1]

        # Snakes
        for i in range(0, len(sn), 2):
            jump[sn[i]] = sn[i + 1]

        visited = [False] * (N + 1)
        q = deque([(1, 0)])
        visited[1] = True

        while q:
            cur, dist = q.popleft()

            if cur == N:
                return dist

            for dice in range(1, 7):
                nxt = cur + dice

                if nxt > N:
                    break

                # Mandatory snake/ladder jump
                if jump[nxt] != -1:
                    nxt = jump[nxt]

                if not visited[nxt]:
                    visited[nxt] = True
                    q.append((nxt, dist + 1))

        return -1