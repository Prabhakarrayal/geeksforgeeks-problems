class Solution:
    def minCost(self, n: int, i: int, d: int, c: int) -> int:
        # code here
        
        dp = [j * i for j in range(n + 1)]
        for j in range(2, n + 1):
            j2 = j // 2
            if j & 1:
                dp[j] = min(dp[j], i + c + dp[j2], d + c + dp[j2 + 1])
            else:
                dp[j] = min(dp[j], c + dp[j2])
        return dp[n]