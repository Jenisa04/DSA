class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # prime numbers are numbers divisible by 1 and themselves
        # no even number is a prime except 2
        # for an odd number
        # run loop till half of that number and divide till 0 is found; if not found, it is prime, otherwise not
        
        if n < 2:
            return 0
        
        primes = [1] * n
        primes[0] = 0
        primes[1] = 0
        i=2
        
        while i<n:
            tmp = i
            if primes[i]:
                tmp += i
                while tmp<n:
                    primes[tmp] = 0
                    tmp += i

            i+=1
        return sum(primes)