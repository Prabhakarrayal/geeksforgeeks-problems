class Solution:
    def findMinCost(self, s1: str, s2: str, costS1: int, costS2: int) -> int:
        n = len(s2)
        total = len(s1) * costS1 + len(s2) * costS2

        dp = [0] * (n + 1)
        save = costS1 + costS2

        for a in s1:
            prev = 0

            for j in range(1, n + 1):
                temp = dp[j]

                if a == s2[j - 1]:
                    dp[j] = prev + save
                elif dp[j - 1] > dp[j]:
                    dp[j] = dp[j - 1]

                prev = temp

        return total - dp[n]