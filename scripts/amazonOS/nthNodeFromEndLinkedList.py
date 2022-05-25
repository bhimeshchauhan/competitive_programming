"""

nth from last

"""


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        # Initialize the head object
        self.head = None

    def insert_node(self, data):

        if data is None:
            return

        # create a node object
        node = Node(data)

        # insert the node at the head
        node.next = self.head
        self.head = node

    def get_head(self):
        # return the current head object
        return self.head

    def display_lst(self):
        """
        Method to print the elements of the linked list
        :return:
        """

        current = self.head

        while current:
            print(current.data, end="->")
            current = current.next

    def get_nth_node(self, n):

        if not self.head or n <= 1:
            return -1

        # initialize both the pointers to
        p1 = self.head
        p2 = self.head

        # move the first pointer n nodes
        for i in range(n):
            p1 = p1.next

        # Move both the pointers till p1 reaches the end of the list
        while p1:
            p1 = p1.next
            p2 = p2.next

        return p2


l = LinkedList()

l.insert_node(10)
l.insert_node(20)
l.insert_node(30)
l.insert_node(40)
l.insert_node(50)
l.insert_node(60)
l.insert_node(70)
l.insert_node(80)

l.display_lst()
print('')
print(l.get_nth_node(2).data)
