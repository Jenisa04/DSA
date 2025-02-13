class Solution:
    # Jenisa
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for tok in tokens:
            if tok in '+-*/':
                if tok == '+':
                    num1 = res.pop()
                    num2 = res.pop()
                    res.append(num2 + num1)
                elif tok == '-':
                    num1 = res.pop()
                    num2 = res.pop()
                    res.append(num2 - num1)
                elif tok == '*':
                    num1 = res.pop()
                    num2 = res.pop()
                    res.append(num2 * num1)
                elif tok == '/':
                    num1 = res.pop()
                    num2 = res.pop()
                    res.append(int(num2 / num1))
            else:
                res.append(int(tok))
        return res[0]