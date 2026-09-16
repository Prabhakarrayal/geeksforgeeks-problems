class Solution:
    def dominantPairs(self, arr: list[int]) -> int:
        n = len(arr) // 2

        left = sorted(arr[:n])
        right = sorted(arr[n:])

        j = 0
        ans = 0

        for x in left:
            while j < n and x >= 5 * right[j]:
                j += 1
            ans += j

        return ans