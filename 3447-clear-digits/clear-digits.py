class Solution:
    # Jenisa
    def clearDigits(self, s: str) -> str:
        # Approach:
        # iterate over s
        # add to stack if alphabet
        # if number, pop from stack 
        output = [] #record stack
        for i in s:
            if i.isalpha():
                output.append(i)
            else:
                output.pop()
        
        if len(output)>0:
            return ''.join(output)
        return ""