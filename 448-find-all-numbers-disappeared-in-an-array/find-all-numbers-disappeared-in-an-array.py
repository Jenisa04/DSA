class Solution:
    # Jenisa
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missing = set(range(1,len(nums)+1)) - set(nums)

        return list(missing)