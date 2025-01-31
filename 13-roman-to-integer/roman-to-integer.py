class Solution:
    # Jenisa
    def romanToInt(self, s: str) -> int:
        num = list(s)
        total = 0
        rom_to_num = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range(len(num)):
            if i+1 < len(num) and rom_to_num[num[i]] < rom_to_num[num[i+1]]:
                total-= rom_to_num[num[i]]
            else:
                total += rom_to_num[num[i]]

        return total