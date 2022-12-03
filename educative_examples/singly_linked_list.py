# Singly Linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __find_a_node__(self, data):
        prev_node = None
        cur_node = self.head
        while cur_node and cur_node.data != data:
            prev_node = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return(None, None)

        return (prev_node, cur_node)

    def __find_last_node__(self):
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        return curr_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node
        return new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Given previous node doesn't exist!")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node        

    def delete_by_data(self, data):
        """
        To solve this problem, we need to handle two cases:
            1. Node to be deleted is head.
            2. Node to be deleted is not head.
        """
        cur_node = self.head
        if cur_node and cur_node.data == data:
            self.head = cur_node.next
            cur_node = None
            return
        prev_node, cur_node = self.__find_a_node__(data)

        if cur_node is None:
            return
        prev_node.next = cur_node.next
        cur_node = None

    def delete_at_pos(self, pos):
        """
        To solve this problem, we need to handle two cases:
            1. Node to be deleted is at pos 0.
            2. Node to be deleted is not at pos 0.
        """
        cur_node = self.head
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return
        index = 0
        prev_node = None
        while cur_node and index != pos:
            prev_node = cur_node
            cur_node = cur_node.next
            index += 1

        if cur_node is None:
            return 
        
        prev_node.next = cur_node.next
        cur_node = None

    def reverse_list(self):
        """
        Algorithm: have two pointers PREV & CURR
        Replace the CURR->next to previous
        Move CURR and PREV one step towards left
        continue this until all elements are processed.
        Finally replaces the head pointer to previous.
        """
        prev_node = None
        cur_node = self.head
        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        self.head = prev_node

    def reverse_list_by_iter(self):
        """
        Algorithm: have two pointers PREV & CURR
        Replace the CURR->next to previous
        Move CURR and PREV one step towards left
        continue this until all elements are processed.
        Finally replaces the head pointer to previous.
        """        
        def _reverse_list_by_iter_internal(prev, curr):
            if curr is None:
                return prev
            next = curr.next
            curr.next = prev
            return _reverse_list_by_iter_internal(curr, next)
        self.head = _reverse_list_by_iter_internal(prev=None, curr=self.head)

    def merge_sorted_list(self, llst):
        """
        Algorithm

        To solve this problem, 
        we’ll use two pointers (p and q) which will each initially point to the head node of each linked list. 
        There will be another pointer, s, that will point to the smaller value of data of the nodes that p and q are pointing to. 
        Once s points to the smaller value of the data of nodes that p and q point to, 
            p or q will move on to the next node in their respective linked list. 
        If s and p point to the same node, p moves forward; otherwise q moves forward. 
        The final merged linked list will be made from the nodes that s keeps pointing to.
        """
        p = self.head
        q = llst.head
        s = None

        if q is None:
            return p
        if p is None:
            return q

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
        self.head = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p
        return self.head

    def length_by_iter(self):
        cur_node = self.head
        node_len = 0
        while cur_node:
            cur_node = cur_node.next
            node_len += 1
        return node_len

    def length_by_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.length_by_recursive(node.next)

    def swap_nodes(self, data1, data2):
        """ Algorithm
        We can start from the first node, i.e., the head node of the linked list and keep track of both the previous and the current node.
        At first - set the current node to the head of the linked list and the previous node to nothing because there’s no previous node to the current node.
        Next, we proceed through the linked list looking at the data elements and checking if the data element of the node that we’re on matches one of the two data.
        f we find the match, we record that information and repeat the same process for the second key that we’re looking for. 
        This is the general way we will keep track of the information.

        There are two cases that we’ll have to cater for
        1. Node 1 and Node 2 are not head nodes
        2. Either Node 1 or Node 2 is a head node
        """
        if data1 == data2:
            print("both data1 and data2 should be different value")
            return
        prev1_node, cur1_node = self.__find_a_node__(data1)
        prev2_node, cur2_node = self.__find_a_node__(data2)

        if not cur1_node or not cur2_node:
            return

        if prev1_node:
            prev1_node.next = cur2_node
        else:
            self.head = cur2_node
        if prev2_node:
            prev2_node.next = cur1_node
        else:
            self.head = cur1_node
        cur2_node.next, cur1_node.next = cur1_node.next, cur2_node.next

    def remove_duplicates(self):
        """
        Algorithm
        The general approach to solve this problem is to loop through the linked list once and keep track of all the data held at each of the nodes. 
        We can use a hash table or Python dictionary to keep track of the data elements that we encounter. 
        For example, if we encounter 6, we will add that to the dictionary or hash table and move along. 
        Now if we meet another 6 and we check for it in our dictionary or hash table, 
            then we’ll know that we already have a 6 and the current node is a duplicate.
        """
        curr_node = self.head
        prev_node = None
        dup_entries = []
        while curr_node:
            if curr_node.data in dup_entries:
                prev_node.next = curr_node.next
                curr_node = None
            else:
                dup_entries.append(curr_node.data)
                prev_node = curr_node
            curr_node = prev_node.next


    def nth_to_last(self, n):
        """
        Algorithm
        We’ll break down this solution in two simple steps:
            1. Calculate the length of the linked list.
            2. Count down from the total length until n is reached.
        For example, if we have a linked list of length four, 
            then we’ll begin from the head node and decrement the calculated length of the linked list by one as we traverse each node in the linked list. 
        We’ll only stop on the node when our count becomes equal to n.
        """
        list_len = self.length_by_iter()
        if n > list_len:
            print(f"Sorry {n} is higher than the size of the list")
            return None

        curr_node = self.head
        while curr_node:
            if list_len == n:
                return curr_node
            curr_node = curr_node.next
            list_len -= 1

    def nth_to_last_with_2ptrs(self, n):
        """
        Algorithm
        There will be a total of two pointers p and q:

            1. p will point to the head node.
            2. q will point n nodes beyond head node.

        Next, we’ll move these pointers along with the linked list one node at a time. 
        When q will reach None, we’ll check where p is pointing, as that is the node we want.
        """
        p = self.head
        q = self.head

        if n > 0:
            qpos = 0
            while q:
                qpos += 1
                if qpos >= n:
                    break
                q = q.next

            if not q:
                print(str(n) + " is greater than the number of nodes in list.")
                return None

            while p and q.next:
                p = p.next
                q = q.next
            return p

        else:
            return None

    def count_occurences_by_iteration(self, data):
        curr_node = self.head
        count = 0
        while curr_node:
            if curr_node.data == data:
                count += 1

            curr_node = curr_node.next
        return count

    def count_occurences_by_recursive(self, data, node):
        if not node:
            return 0
        elif node.data == data:
            return 1 + self.count_occurences_by_recursive(data, node.next)
        else:
            return self.count_occurences_by_recursive(data, node.next)

    def rotate_nodes_by_pivot(self, pivot):
        not_used, pivot_node = self.__find_a_node__(pivot)
        if not pivot_node:
            print("Couldn't find a pivot node")
            return
        last_node = self.__find_last_node__()
        last_node.next = self.head
        self.head = pivot_node.next
        pivot_node.next = None
 