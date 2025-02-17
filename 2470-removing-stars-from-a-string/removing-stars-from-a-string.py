class Solution:
    # Jenisa
    def removeStars(self, s: str) -> str:
        rec = []
        for char in s:
            if char == '*':
                rec.pop()
            else:
                rec.append(char)

        return ''.join(rec[::])