class Solution:
    def minMoves(self, arr):
        n = len(arr)

        pos = [0] * (n + 1)

        for i, value in enumerate(arr):
            pos[value] = i

        longest = 1
        current = 1

        for value in range(1, n):
            if pos[value] < pos[value + 1]:
                current += 1
                longest = max(longest, current)
            else:
                current = 1

        return n - longest