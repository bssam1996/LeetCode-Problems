"""
Link: https://leetcode.com/problems/implement-stack-using-queues/
"""


class MyStack:

    def __init__(self):
        self.mystack = []

    def push(self, x: int):
        self.mystack.append(x)
        return None

    def pop(self) -> int:
        return self.mystack.pop()

    def top(self) -> int:
        return self.mystack[-1]

    def empty(self) -> bool:
        return len(self.mystack) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
