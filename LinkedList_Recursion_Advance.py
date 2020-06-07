class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def print_me(self, current):
        if current:
            print(current.data)
            self.print_me(current.next)

    def append(self, current, data):
        if current.next:
            self.append(current.next, data)
        else:
            current.next = Node(data)

    def remove(self, data, previous):
        if self.data == data:
            previous.next = self.next
        else:
            self.next.remove(data, self)


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def print_list(self):
        self.head.print_me(self.head)
        # self._print(self.head)

    def _print(self, current):
        if current:
            print(current.data)
            self._print(current.next)

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        self.head.append(self.head, data)

    def remove(self, data):
        if self.head.data == data:
            self.head = self.head.next
        else:
            self.head.next.remove(data, self.head)


llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.remove(5)
llist.print_list()

