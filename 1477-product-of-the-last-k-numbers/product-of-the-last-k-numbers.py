class ProductOfNumbers:
    # Jenisa
    def __init__(self):
        self.nums = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.nums = []
            self.nums.append(1)
        else:
            self.nums.append(self.nums[-1] * num)
           
    def getProduct(self, k: int) -> int:
        if k >= len(self.nums):
            return 0
        else:
            num1 = self.nums[len(self.nums) - 1 - k]
            num2 = self.nums[-1]
            return int(num2/num1)


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)