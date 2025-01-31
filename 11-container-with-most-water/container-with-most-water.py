class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxArea = 0
        while l<r:
            minHeight = min(height[l], height[r])
            if maxArea < minHeight * (r-l):
                maxArea = minHeight * (r-l)
            if height[l] > height[r]:
                r-=1
            else:
                l+=1
        return maxArea