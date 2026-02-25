from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()          # main queue
        self.helper = deque()     # temporary queue (can be avoided in one-queue version)

    def push(self, x: int) -> None:
        # Move all elements from main queue to helper
        while self.q:
            self.helper.append(self.q.popleft())
        
        # Add new element to main queue (it becomes the "top")
        self.q.append(x)
        
        # Move everything back from helper to main queue
        while self.helper:
            self.q.append(self.helper.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your input test:
# ["MyStack","push","push","top","pop","empty"]
# [[],[1],[2],[],[],[]]
# Output: [null,null,null,2,2,false]