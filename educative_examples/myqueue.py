# Queue Implementation

class Queue:
    def __init__(self) -> None:
        self.items = []
    
    def enqueue(self, value):
        self.items.insert(0, value)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return True if len(self.items) == 0 else False

    def size(self):
        return len(self.items)

    def __len__(self):
        return self.size()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

# queue = Queue()
# queue.enqueue(10)
# queue.enqueue(20)
# print(queue.dequeue())
# print( queue.is_empty() )
# print (queue.size())
# print(queue.peek())
# print(queue.dequeue())
# print( queue.is_empty() )


    
