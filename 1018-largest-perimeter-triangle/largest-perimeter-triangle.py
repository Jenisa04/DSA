class Solution(object):
    # Jenisa
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # for 3 sides to form a triangle, sum of any 2 sides must be greater than remaining 1 side
        # [2,1,2]: 2+1>2, 1+2>2, and 2+2>1 so it is a triangle
        # if any sum turns to be false, no triangle can be formed

        nums.sort()
        for i in range(len(nums) - 1, 1, -1):
            # c = nums[i - 1] + nums[i - 2]
            if (nums[i - 1] + nums[i - 2] > nums[i]):
                return nums[i - 1] + nums[i - 2] + nums[i]

        return 0       