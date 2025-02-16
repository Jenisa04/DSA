class Solution:
    # Jenisa
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        atP = set(nums)
        missing = []

        for i in range(1, len(nums)+1):
            if i not in atP:
                missing.append(i)

        return missing