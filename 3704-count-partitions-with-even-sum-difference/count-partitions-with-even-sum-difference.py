class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        prefixSum = [nums[0]]
        total = sum(nums)
        count = 0
        for i in range(1,len(nums)):
            prefixSum.append(prefixSum[i-1] + nums[i])
            rightSum = total - prefixSum[i-1]
            diff = prefixSum[i-1] - rightSum
            if diff%2==0:
                count+=1
        
        return count