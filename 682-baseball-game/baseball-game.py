class Solution:
    # Jenisa
    def calPoints(self, operations: List[str]) -> int:
        recordStack = []
        for i in operations:
            if i == '+':
                res = recordStack[-1] + recordStack[-2]
                recordStack.append(res)
            elif i == 'D':
                res = recordStack[-1] * 2
                recordStack.append(res)
            elif i == 'C':
                recordStack.pop()
            else:
                recordStack.append(int(i))

        return sum(recordStack)