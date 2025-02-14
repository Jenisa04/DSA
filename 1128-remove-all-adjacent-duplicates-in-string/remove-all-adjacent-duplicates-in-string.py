class Solution:
    #Jenisa
    def removeDuplicates(self, s: str) -> str:
        final = []
        for i in s:
            if len(final)>0:
                if i == final[-1]:
                    final.pop()
                else:
                    final.append(i)
            else:
                final.append(i)
        
        return ''.join(final[::])