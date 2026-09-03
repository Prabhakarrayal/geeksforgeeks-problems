class Solution:
    def maxDiffSum(self, arr):
        dp0 = 0
        dp1 = 0

        for i in range(1, len(arr)):
            new0 = max(
                dp0 + abs(arr[i] - arr[i - 1]),
                dp1 + abs(arr[i] - 1)
            )

            new1 = max(
                dp0 + abs(1 - arr[i - 1]),
                dp1
            )

            dp0 = new0
            dp1 = new1

        return max(dp0, dp1)