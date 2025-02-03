class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        leftPtr, totalTime = 0, 0
        # since leftptr starts at index 0, rightptr has to be 1 ahead of it
        for rightPtr in range(1,len(colors)):
            # check for consecutive colors
            if colors[leftPtr] == colors[rightPtr]:
                # check which one takes minimum time
                # eliminate the minimum time one and move the ptr accordingly
                if neededTime[leftPtr] > neededTime[rightPtr]:
                    totalTime += neededTime[rightPtr]
                else:
                    totalTime += neededTime[leftPtr]
                    leftPtr = rightPtr
            else:
                leftPtr = rightPtr

        return totalTime