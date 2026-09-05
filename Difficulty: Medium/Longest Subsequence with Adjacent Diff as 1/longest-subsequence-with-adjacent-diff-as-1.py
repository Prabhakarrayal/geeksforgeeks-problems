class Solution:
    def longestSubseq(self, arr):
            dp = {}
            ans = 0

            for x in arr:
                length = max(dp.get(x - 1, 0), dp.get(x + 1, 0)) + 1
                dp[x] = max(dp.get(x, 0), length)
                ans = max(ans, dp[x])

            return ans
        