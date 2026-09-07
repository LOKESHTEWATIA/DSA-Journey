class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        # dp[i] stores the number of distinct subsequences ending with character i
        dp = [0] * 26

        for ch in s:
            idx = ord(ch) - 97
            dp[idx] = (sum(dp) + 1) % MOD

        return sum(dp) % MOD