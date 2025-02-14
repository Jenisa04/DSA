class Solution:
    # Jenisa
    def finalPrices(self, prices: List[int]) -> List[int]:
        pricesStack = [0]
        answer = []
        for p in prices[::-1]:
            while pricesStack[-1]>p:
                pricesStack.pop()
            answer.append(p-pricesStack[-1])
            pricesStack.append(p)
        
        return answer[::-1]