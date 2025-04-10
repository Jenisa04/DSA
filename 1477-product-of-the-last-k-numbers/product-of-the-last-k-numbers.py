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
            return int(self.nums[-1]/self.nums[len(self.nums) - 1 - k])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)