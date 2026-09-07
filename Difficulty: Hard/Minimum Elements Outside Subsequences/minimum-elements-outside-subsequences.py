class Solution:
    def minCount(self, arr):
        from functools import cache
        @cache
        def dp(ix=len(arr)-1,p1=float('inf'),p2=-float('inf')):
            nonlocal arr
            if ix<0:
                return 0
            mn=float('inf')
            if arr[ix]<p1:
                mn=min(mn,dp(ix-1,arr[ix],p2))
            if arr[ix]>p2:
                mn=min(mn,dp(ix-1,p1,arr[ix]))
            return min(mn,1+dp(ix-1,p1,p2))
        return dp()

