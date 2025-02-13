import heapq
class Solution:
    # Jenisa
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if k > len(matrix) | len(matrix)<1:
            return 

        h = []
        heapq.heapify(h)
        n = len(matrix)
        for row in range(n):
            for col in range(n):
                heapq.heappush(h, -1 * matrix[row][col])
        count = len(h) - k
        while count >= 0:
            num = heapq.heappop(h)
            count-=1
        return -num