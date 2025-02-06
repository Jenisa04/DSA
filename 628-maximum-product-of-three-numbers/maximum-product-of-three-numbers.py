class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        if nums[0] * math.prod(nums[-2:]) > math.prod(nums[:3]):
            return nums[0] * math.prod(nums[-2:])
        return math.prod(nums[:3])