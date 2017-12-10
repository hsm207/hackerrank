class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        if head:
            head.next = self.insert(head.next, data)
            return head
        else:
            return Node(data)



mylist = Solution()
T = 5
head = None
for i in range(T):
    data = i
    head = mylist.insert(head, data)

mylist.display(head)
