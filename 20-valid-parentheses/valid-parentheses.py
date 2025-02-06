class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {')':'(','}':'{',']':'['}
        for char in s:
            if char in ['(','{','[']:
                stack.append(char)
            else:
                try:
                    if dict[char] != stack[-1]:
                        return False
                    else:
                        stack.pop()
                except:
                    return False
        return stack == []