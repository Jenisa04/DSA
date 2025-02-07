class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for num1, num2 in zip(nums, nums[1:]):
            if num1%2==0 and num2%2==0:
                return False
            elif num1%2!=0 and num2%2!=0:
                return False
            else:
                continue
        return True