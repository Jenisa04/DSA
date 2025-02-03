class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rightProd = [1] * len(nums)
        leftProd = [1]
        
        if len(nums) == 2:
            nums[0], nums[1] = nums[1], nums[0]
            return nums
        for i in range(len(nums)-1):
            leftProd.append(leftProd[i] * nums[i])
        for j in range(len(nums)-2, -1, -1):
            rightProd[j] =  rightProd[j+1] * nums[j+1]
        answer = []
        for idx in range(len(nums)):
            answer.append(leftProd[idx] * rightProd[idx])
        
        return answer