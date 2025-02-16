class Solution:
    # Jenisa
    def missingNumber(self, nums: List[int]) -> int:

        diff = abs(sum(range(len(nums)+1)) - sum(nums))
        return diff