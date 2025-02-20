class Solution:
    # Jenisa
    def myPow(self, x: float, n: int) -> float:
        # Recursion approach
        def recursion(base, exponent):
            if exponent == 0:
                return 1
            elif exponent % 2 == 0:
                return recursion(base*base, exponent//2)
            else:
                return base * recursion(base*base, (exponent-1) // 2)
            
        res = recursion(x, abs(n))

        return res if n>=0 else 1/res