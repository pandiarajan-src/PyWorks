# Basic stack implementation

class Stack:
    def __init__(self):
        self.items = list()
    
    def is_empty(self):
        return True if len(self.items) == 0 else False
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            return None

    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]
        else:
            return None        

    def get_stack(self):
        return self.items
