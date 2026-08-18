class Solution:
    def compress(self, s):
    # code here

        n = len(s)
        stack = []
        while n > 0:
            if s[:n//2] == s[n//2:n]:
                stack.append('*')
                n //= 2
            else:
                n -= 1
                stack.append(s[n])
        return "".join(reversed(stack))