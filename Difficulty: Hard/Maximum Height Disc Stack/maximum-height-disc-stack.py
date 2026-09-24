class Solution:
    def maxStackHeight(self, r, h):
        a = sorted(zip(r, h))
        bit = [0] * 1002
        ans = 0

        def query(x):
            z = 0
            while x:
                z = max(z, bit[x])
                x -= x & -x
            return z

        def update(x, v):
            while x <= 1000:
                bit[x] = max(bit[x], v)
                x += x & -x

        i = 0
        while i < len(a):
            j = i
            while j < len(a) and a[j][0] == a[i][0]:
                j += 1

            v = []
            for k in range(i, j):
                height = a[k][1]
                v.append((height, query(height - 1) + height))

            for x, val in v:
                update(x, val)
                ans = max(ans, val)

            i = j

        return ans