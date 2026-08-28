class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or s == s[::-1]:
            return s

        start, max_len = 0, 1

        for i in range(len(s)):
            # Odd-length palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_len:
                    start = l
                    max_len = r - l + 1
                l -= 1
                r += 1

            # Even-length palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_len:
                    start = l
                    max_len = r - l + 1
                l -= 1
                r += 1

        return s[start:start + max_len]