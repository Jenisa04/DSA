class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x>=0 and x<=9:
            return True

        temp = list(str(x))
        temp = int(''.join(temp[::-1]))
        if x==temp:
            return True
        return False