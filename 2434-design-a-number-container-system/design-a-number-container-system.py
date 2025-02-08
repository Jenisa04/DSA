import heapq

class NumberContainers:

    def __init__(self):
        self.nc = dict()   # maps index to number
        self.nc2 = dict()  # maps number to a min-heap of indices

    def change(self, index: int, number: int) -> None:
        # If the index already has a number, remove it from the old number's heap
        if index in self.nc:
            old_num = self.nc[index]
            if old_num in self.nc2:
                # Remove the index from the old number's heap
                pass  # We'll handle this in the find method

        # Update the index to the new number
        self.nc[index] = number

        # Add the index to the new number's heap
        if number not in self.nc2:
            self.nc2[number] = []
        heapq.heappush(self.nc2[number], index)

    def find(self, number: int) -> int:
        if number in self.nc2:
            # Remove any indices from the heap that no longer correspond to this number
            while self.nc2[number] and self.nc[self.nc2[number][0]] != number:
                heapq.heappop(self.nc2[number])
            # If the heap is not empty, return the smallest index
            if self.nc2[number]:
                return self.nc2[number][0]
        return -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index, number)
# param_2 = obj.find(number)