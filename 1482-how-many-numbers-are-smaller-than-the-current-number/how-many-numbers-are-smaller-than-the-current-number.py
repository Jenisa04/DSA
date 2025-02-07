class Solution:
    # Jenisa
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        numsList = sorted(nums)
        n = len(numsList)

        numMap = {}
        res = []

        for i in range(n):
            if numsList[i] not in numMap:
                numMap[numsList[i]] = i
                
        for j in range(len(nums)):
            res.append(numMap[nums[j]])
            
        return res
