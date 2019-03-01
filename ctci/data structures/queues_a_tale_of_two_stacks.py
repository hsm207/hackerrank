class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def peek(self):
        if self.stack2:
            return self.stack2[-1]
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.peek()

    def pop(self):
        # always pop stack2. If it is empty, populate it by pop each element in stack1 and push it into stack2
        if self.stack2:
            self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            self.pop()

    def put(self, value):
        # always dump all inputs into stack1
        self.stack1.append(value)


queue = MyQueue()
# t = int(input())
sample_inputs = ['1 42', '2', '1 14', '3', '1 28', '3', '1 60', '1 78', '2', '2']
for line in sample_inputs:
    values = map(int, line.split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
