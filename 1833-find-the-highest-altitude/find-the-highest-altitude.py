class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # need a prefix sum array
        prefSum = [0]
        for i in range(len(gain)):
            prefSum.append(prefSum[i]+gain[i])
        return max(prefSum)