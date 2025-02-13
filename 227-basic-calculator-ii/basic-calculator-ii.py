class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        s = list(s)
        currVal = 0
        n = len(s)
        prevSign = '+'
        numStack = []
        
        for idx, val in enumerate(s):
            if val.isdigit():
                currVal = currVal * 10 + int(val)
                
            if idx==n-1 or val in '+-*/':
                if prevSign == '+':
                    numStack.append(currVal)
                elif prevSign == '-':
                    numStack.append(-currVal)
                elif prevSign == '*':
                    res = numStack.pop() * currVal
                    numStack.append(res)
                elif prevSign == '/':
                    res = numStack.pop() / currVal
                    numStack.append(int(res))

                prevSign = val
                currVal = 0
        
        return sum(numStack)
            
