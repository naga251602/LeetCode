class Solution:
    def fib(self, n: int) -> int:
        m = defaultdict()
        def f(n):
            if n == 0: return 0
            if n == 1: return 1
            if m.get(n, -1) != -1: return m.get(n)
            m[n] = f(n-1) + f(n-2)

            return m[n]
        return f(n)