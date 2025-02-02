class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # approach: calculate left and right sum together
        # calculate total sum of the arrray first
        totalSum = sum(nums)
        # Given: left edge sum = 0 so
        leftSum = 0
        # iterate over nums now
        for idx, num in enumerate(nums):
            # calculate rightSum first which would be total sum - leftSum - the number at current index too since we want the sum of all indices on the right of current index
            rightSum = totalSum - leftSum - num
            
            # check if leftSum and rightSum are equal
            if leftSum == rightSum:
                return idx
            
            leftSum += num
        # if no pivot found, return -1
        return -1