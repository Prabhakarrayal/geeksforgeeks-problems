class Solution:
    def solve(self, n, s):
        active = set()
        rejected = set()
        ans = 0

        for ch in s:
            if ch in active:
                active.remove(ch)
            elif ch in rejected:
                rejected.remove(ch)
            else:
                if len(active) < n:
                    active.add(ch)
                else:
                    rejected.add(ch)
                    ans += 1

        return ans