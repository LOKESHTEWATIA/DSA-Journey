class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        x = 0
        digit_sum = 0
        
        s = str(n)
        for char in s:
            if char != '0':
                digit = int(char)
                x = x * 10 + digit
                digit_sum += digit
        return x * digit_sum if x > 0 else 0