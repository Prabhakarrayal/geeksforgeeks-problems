from functools import lru_cache

class Solution:
    def countWithout(self, n: int, d: int) -> int:
        digits = str(n)

        @lru_cache(None)
        def dp(pos, tight, started):
            if pos == len(digits):
                return int(started)

            limit = int(digits[pos]) if tight else 9
            ans = 0

            for x in range(limit + 1):
                next_tight = tight and (x == int(digits[pos]))

                # Still in leading zeroes.
                if not started and x == 0:
                    ans += dp(pos + 1, next_tight, False)

                # Actual digit: forbidden digit cannot be used.
                elif x != d:
                    ans += dp(pos + 1, next_tight, True)

            return ans

        return dp(0, True, False)