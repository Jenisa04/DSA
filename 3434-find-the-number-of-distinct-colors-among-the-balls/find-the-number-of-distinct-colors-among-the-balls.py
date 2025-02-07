class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ballToCol = dict()
        colToBall = dict()
        result = []
        for i, j in queries:
            if i in ballToCol:
                oldCol = ballToCol[i]
                colToBall[oldCol].remove(i)

                if not colToBall[oldCol]:
                    del colToBall[oldCol]
            
            ballToCol[i] = j
            if j not in colToBall:
                colToBall[j] = set()
            colToBall[j].add(i) 
            result.append(len(colToBall))           
        return result