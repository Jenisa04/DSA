class Solution:
    # Jenisa
    def subarraySum(self, nums: List[int]) -> int:
        preNum = [nums[0]]
        for i in range(1,len(nums)):
            preNum.append(preNum[i-1] + nums[i])

        res = 0
        for j in range(len(nums)):
            start = max(0, j-nums[j])
            if start != 0:
                res += (preNum[j] - preNum[start-1])
            else:
                res += preNum[j]

        return res