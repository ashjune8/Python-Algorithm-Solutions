class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items = []


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.items.insert(0,x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.items.pop(0)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.items[0]


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.items == []



        # Your MyStack object will be instantiated and called as such:
        # obj = MyStack()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.empty()