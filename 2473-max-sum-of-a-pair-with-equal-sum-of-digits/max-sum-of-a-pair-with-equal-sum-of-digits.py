from typing import List

class Solution:
    def digitSum(self, num: int) -> int:
        return sum(int(digit) for digit in str(num))  # Faster way to compute digit sum
    
    def maximumSum(self, nums: List[int]) -> int:
        digitSumMap = {}  # Maps digit sum to the two largest numbers with that sum
        maxSum = -1
        
        for num in nums:
            dSum = self.digitSum(num)
            
            if dSum not in digitSumMap:
                digitSumMap[dSum] = [num, -1]  # Store two largest numbers (initialized as -1)
            else:
                # Update the two largest numbers for this digit sum
                if num > digitSumMap[dSum][0]:
                    digitSumMap[dSum][1] = digitSumMap[dSum][0]
                    digitSumMap[dSum][0] = num
                elif num > digitSumMap[dSum][1]:
                    digitSumMap[dSum][1] = num
        
        # Compute max pair sum from stored values
        for largest, secondLargest in digitSumMap.values():
            if secondLargest != -1:  # Only consider pairs with at least two numbers
                maxSum = max(maxSum, largest + secondLargest)
        
        return maxSum
