class Solution:
    def pairAndSum(self, arr):
        # code here
        ans = 0
        
        for b in range(31):
            cnt = 0
            mask = 1 << b
            
            for x in arr:
                if x & mask:
                    cnt += 1
                    
            ans += cnt * (cnt - 1) // 2 * mask
            
        return ans