class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        return self.items.insert(0, x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.items.pop(len(self.items) - 1)

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.items[len(self.items) - 1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.items) == 0:
            return True
        else:
            return False



            # Your MyQueue object will be instantiated and called as such:
            # obj = MyQueue()
            # obj.push(x)
            # param_2 = obj.pop()
            # param_3 = obj.peek()
            # param_4 = obj.empty()