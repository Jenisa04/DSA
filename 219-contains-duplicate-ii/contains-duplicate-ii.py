class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        temp = {}
        for i, num in enumerate(nums):
            if num in temp and i - temp[num] <=k:
                return True
            # save index of the num 
            temp[num] = i
        return False