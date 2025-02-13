class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # record 2 stacks each, s and t
        # for every '#', check the len(record stacks)
        sRec = []
        tRec = []
        for i in s:
            if i == '#':
                if len(sRec) == 0:
                    continue
                else:
                    sRec.pop()
            else:
                sRec.append(i)
        
        for j in t:
            if j == '#':
                if len(tRec) == 0:
                    continue
                else:
                    tRec.pop()
            else:
                tRec.append(j)
        
        if sRec==tRec:
            return True
        return False