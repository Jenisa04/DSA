class Solution:
    # Jenisa
    def containsDuplicate(self, nums: List[int]) -> bool:
        rec = set()
        for i in nums:
            if i in rec:
                return True
            rec.add(i)
        return False