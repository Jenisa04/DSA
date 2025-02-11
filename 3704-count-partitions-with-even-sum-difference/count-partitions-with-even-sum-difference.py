class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        prefixSum = [nums[0]]
        total = sum(nums)
        rightSum = [total]

        for i in range(1,len(nums)):
            prefixSum.append(prefixSum[i-1] + nums[i])
            rightSum.append(total - prefixSum[i-1])
        
        count = 0
        for j in range(1, len(nums)):
            diff = prefixSum[i-1] - rightSum[i]
            if diff%2==0:
                count+=1
        
        return count