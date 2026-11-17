class FreqStack:
    """
    stacks = {maxCount: [nums]}
    store every nums base on the freq it exist 
    """
    def __init__(self):
        self.maxCount = 0
        self.cnt = {}
        self.stacks = {} # occurance time of each numbers 

    def push(self, val: int) -> None:
        count = self.cnt.get(val, 0) + 1
        self.cnt[val] = count

        if count > self.maxCount:
            self.maxCount = count
            self.stacks[count] = []

        self.stacks[count].append(val)

    def pop(self) -> int:
        res = self.stacks[self.maxCount].pop()
        self.cnt[res] -= 1
        if not self.stacks[self.maxCount]:
            self.maxCount -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()