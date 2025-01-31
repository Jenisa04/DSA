class Solution:
    # Jenisa
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] + 1 < 10:
            digits[-1] = digits[-1] + 1
        else:
            count = 0
            i = len(digits) - 1
            while (digits[i] + 1) > 9:
                count += 1
                i -= 1
                if i < 0:
                    break
            if count >= len(digits): 
                digits = [0] * (count + 1)
                digits[0] += 1
            else:
                digits[-count::] = [0] * count
                digits[-(count+1)] += 1
        return digits