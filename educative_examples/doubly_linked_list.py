# Doubly linked lists

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedLists:
    def __init__(self):
        self.head = None

    def __find_a_data_node(self, data):
        curr_node = self.head
        while curr_node and curr_node.data != data:
            curr_node = curr_node.next
        return curr_node


    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=", ")
            curr_node = curr_node.next
        print("\n======")

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node and curr_node.next != None:
                curr_node = curr_node.next

            curr_node.next = new_node
            new_node.prev = curr_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            curr_node = self.head
            curr_node.prev = new_node
            new_node.next = curr_node
            self.head = new_node

    def add_after_node(self, key, data):
        curr_node = self.__find_a_data_node(key)
        if not curr_node:
            print(f"Sorry {key} node can't be found in the list")
            return
        if not curr_node.next: # This is the tail node
            self.append(data)
            return 
        new_node = Node(data)
        next_node = curr_node.next
        new_node.prev = curr_node
        new_node.next = next_node
        curr_node.next = new_node
        next_node.prev = new_node

    def add_before_node(self, key, data):
        curr_node = self.__find_a_data_node(key)
        if not curr_node:
            print(f"Sorry {key} node can't be found in the list")
            return
        if not curr_node.prev: # This is the head node
            self.prepend(data)
            return 
        new_node = Node(data)
        prev_node = curr_node.prev
        new_node.next = curr_node
        new_node.prev = prev_node
        prev_node.next = new_node
        curr_node.prev = new_node

    def delete_node(self, node):
        if not node.next and not node.prev: # There is only one node
            node = None
            self.head = None
        elif not node.prev: # This is head node
            new_head = node.next
            new_head.prev = None
            node = None
            self.head = new_head
        elif not node.next: # This is tail node
            new_tail = node.prev
            new_tail.next = None
            node = None
        else:
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            node = None       

    def delete(self, key):
        curr_node = self.__find_a_data_node(key)
        if not curr_node:
            print(f"Sorry {key} not found in the list")
            return
        self.delete_node(curr_node)

    def reverse(self):
        curr_node = self.head
        while curr_node:
            next_node = curr_node.next
            prev_node = curr_node.prev
            if not curr_node.prev: # This is head node
                curr_node.prev = next_node
                curr_node.next = None
            elif not curr_node.next: # This is tail node
                curr_node.prev = None
                curr_node.next = prev_node
                self.head = curr_node
            else:
                curr_node.prev = next_node
                curr_node.next = prev_node
            curr_node = next_node

    def remove_duplicates(self):
        unique_lst = []
        curr_node = self.head
        while curr_node:
            if curr_node.data in unique_lst:
                self.delete_node(curr_node)
            else:
                unique_lst.append(curr_node.data)
            curr_node = curr_node.next


def basic_doubly_linklist_test():
    dllst = DoubleLinkedLists()
    # Test for append and prepend
    dllst.append(30)
    dllst.append(40)
    dllst.append(50)
    dllst.prepend(20)
    dllst.prepend(10)
    dllst.print_list()

    # Test for add before and add after
    dllst.add_before_node(10, 0)
    dllst.add_after_node(50, 60)
    dllst.add_after_node(20, 25)
    dllst.add_before_node(20, 15)
    dllst.print_list()

    # Test for delete
    dllst.delete(0)
    dllst.delete(60)
    dllst.delete(15)
    dllst.delete(25)
    dllst.print_list()

    # Test for reverse
    dllst.reverse()
    dllst.print_list()

    # simple test
    dllst1 = DoubleLinkedLists()
    dllst1.prepend(10)
    dllst1.prepend(10)
    dllst1.append(20)
    dllst1.append(20)
    dllst1.print_list()

    dllst1.remove_duplicates()
    dllst1.print_list()

    dllst1.delete(10)
    dllst1.delete(20)
    dllst1.print_list()

    dllst2 = DoubleLinkedLists()
    dllst2.append(2)
    dllst2.append(2)
    dllst2.append(2)
    dllst2.append(2)
    dllst2.print_list()
    dllst2.remove_duplicates()
    dllst2.print_list()


