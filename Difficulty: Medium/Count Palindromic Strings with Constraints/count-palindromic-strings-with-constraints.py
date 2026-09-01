class Solution:
    def palindromicStrings(self, n, k):
        # code here
        MOD = 10**9 + 7

        ans = 0
        perm = 1  # P(k, 0)

        for m in range(k + 1):
            # Length = 2m
            if m > 0 and 2 * m <= n:
                perm = perm * (k - m + 1) % MOD
                ans = (ans + perm) % MOD

            # Length = 2m + 1
            if 2 * m + 1 <= n and m < k:
                ans = (ans + perm * (k - m)) % MOD

        return ans