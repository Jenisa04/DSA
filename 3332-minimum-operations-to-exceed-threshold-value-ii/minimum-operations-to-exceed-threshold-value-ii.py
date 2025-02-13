import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) >= k:
            return 0
        
        if len(nums) < 2:
            return 0

        heapq.heapify(nums)
        ops = 0
        i = 0
        while i<len(nums):
            x = heapq.heappop(nums)
            if x<k:
                y = heapq.heappop(nums)
                res = x*2 + y
                heapq.heappush(nums, res)
                ops+=1
            else:
                break

        return ops