class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rightProd = [1] * len(nums)
        leftProd = [1]
        answer = []
        if len(nums) == 2:
            nums[0], nums[1] = nums[1], nums[0]
            return nums

        for j in range(len(nums)-2, -1, -1):
            rightProd[j] =  rightProd[j+1] * nums[j+1]
        
        for i in range(len(nums)):
            leftProd.append(leftProd[i] * nums[i])
            answer.append(rightProd[i] * leftProd[i])
        
        return answer