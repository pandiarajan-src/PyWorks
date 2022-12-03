# Circular Linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        if self.head:
            count = 1
        else:
            count  = 0
        last_node = self.head
        while last_node and last_node.next != self.head:
            count += 1
            last_node = last_node.next
        return count        

    def __find_a_last_node__(self):
        last_node = self.head
        while last_node and last_node.next != self.head:
            last_node = last_node.next
        return last_node

    def __find_a_node__(self, data):
        prev_node = None
        curr_node = self.head
        while curr_node and curr_node.data != data:
            prev_node = curr_node
            curr_node = curr_node.next
            if curr_node == self.head:
                curr_node = None
                break
        if not curr_node:
            return (None, None, False)
        if not prev_node:
            """This condition will fall when the curr_node is self.head"""
            last_node = self.__find_a_last_node__()
            return (last_node, curr_node, True)

        return (prev_node, curr_node, False)
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            last_node = self.__find_a_last_node__()
            last_node.next = new_node
            new_node.next = self.head

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(f"{curr_node.data}", end=", ")
            curr_node = curr_node.next
            if curr_node == self.head:
                break
        print("\n===============")
        
    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        
        last_node = self.__find_a_last_node__()
        last_node.next = new_node
        new_node.next = self.head
        self.head = new_node

    def remove(self, data):
        """
        The occurrences of nodes will be unique, 
            i.e., there will be no duplicate nodes in the circular linked list that we’ll test on.
        """
        prev_node, curr_node, is_head = self.__find_a_node__(data)
        if not curr_node:
            return
        prev_node.next = curr_node.next
        if is_head:
            if prev_node == curr_node:
                """This will happen if the node is having just one node"""
                self.head = None
            else:
                self.head = curr_node.next
        curr_node = None

    def split_list(self):
        length = self.__len__()
        if length < 2:
            """if list size is 0 or 1 then return 2nd list as none"""
            return None
        mid = length // 2
        curr_node = self.head
        count = 1
        while curr_node and count < mid:
            curr_node = curr_node.next
            count += 1
        
        cllst = CircularLinkedList()
        cllst.head = curr_node.next
        cllst_curr_node = cllst.head
        while cllst_curr_node and cllst_curr_node.next != self.head:
            cllst_curr_node = cllst_curr_node.next

        cllst_curr_node.next = cllst.head

        curr_node.next = self.head
        return cllst

def cllst_split_list_test():
    cllst = CircularLinkedList()
    cllst.append(30)
    cllst.append(40)
    cllst.append(50)
    cllst.prepend(20)
    cllst.prepend(10)
    cllst.print_list()
    print("going to split the list into half")
    new_cllst = cllst.split_list()
    print("old list")
    cllst.print_list()
    print("new list")
    new_cllst.print_list()

    # Test Empty list
    e_cllst = CircularLinkedList()
    print("going to split the list into half")
    new_e_cllst = e_cllst.split_list()
    print("old list")
    e_cllst.print_list()
    if new_e_cllst:
        print("new list")
        new_e_cllst.print_list()
    else:
        print("new list is NONE")

    # Test one node list
    o_cllst = CircularLinkedList()
    o_cllst.append(10)
    print("going to split the list into half")
    new_o_cllst = o_cllst.split_list()
    print("old list")
    o_cllst.print_list()
    if new_o_cllst:
        print("new list")
        new_o_cllst.print_list()   
    else:
        print("new list is NONE")       

    # Test even node list
    ev_cllst = CircularLinkedList()
    ev_cllst.append(10)
    ev_cllst.append(20)

    print("going to split the list into half")
    new_ev_cllst = ev_cllst.split_list()
    print("old list")
    ev_cllst.print_list()
    if new_ev_cllst:
        print("new list")
        new_ev_cllst.print_list()   
    else:
        print("new list is NONE")          


def cllst_remove_test():
    cllst = CircularLinkedList()
    cllst.append(30)
    cllst.append(40)
    cllst.append(50)
    cllst.prepend(20)
    cllst.prepend(10)
    cllst.print_list()
    print("going to remove head node")
    cllst.remove(10)
    cllst.print_list()
    print("going to remove tail node")
    cllst.remove(50)
    cllst.print_list() 
    print("going to remove middle node")
    cllst.remove(30)
    cllst.print_list()

    cllst1 = CircularLinkedList()
    cllst1.append(10)
    cllst1.print_list()
    cllst1.remove(10)
    cllst1.print_list()


def circular_linked_list_basic_test():
    cllst = CircularLinkedList()
    cllst.append(30)
    cllst.append(40)
    cllst.append(50)
    cllst.prepend(20)
    cllst.prepend(10)
    cllst.print_list()
    print(f"Length of Circular linked list : {len(cllst)}")
    cllst1 = CircularLinkedList()
    cllst1.prepend(20)
    cllst1.prepend(10)
    cllst1.append(30)
    cllst1.append(40)
    cllst1.append(50)
    cllst1.print_list()
