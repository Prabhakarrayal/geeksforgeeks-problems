class Solution:
    def minProd(self, arr):
        n = len(arr)
        ans = float('inf')

        for mask in range(1, 1 << n):
            product = 1

            for i in range(n):
                if mask & (1 << i):
                    product *= arr[i]

            ans = min(ans, product)

        return ans