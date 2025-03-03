class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        sm = []
        bg = []
        pvt = []
        for num in nums:
            if num<pivot:
                sm.append(num)
            elif num>pivot:
                bg.append(num)
            else:
                pvt.append(num)
        return sm+pvt+bg