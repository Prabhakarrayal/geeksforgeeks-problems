class Solution:
    def prefixStrings(self, n: int) -> int:
        MOD = 10**9 + 7

   
        numerator = 1
        denominator = 1

        for i in range(1, n + 1):
            numerator = numerator * (n + i) % MOD
            denominator = denominator * i % MOD

   
        comb = numerator * pow(denominator, MOD - 2, MOD) % MOD

    
        return comb * pow(n + 1, MOD - 2, MOD) % MOD