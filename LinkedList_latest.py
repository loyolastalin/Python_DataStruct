
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        prev = None
        while current:
            
            if current.data == data:
                prev.next = current.next
            prev = current
            current = current.next

    def merge_list(self, llist):
        p = self.head
        q = llist.head
        s = None
        if p.data <= q.data:
            s = p
            p = p.next
        else:
            s = q
            q = q.next
        head_node = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = p.next
            else:
                s.next = q
                s = q
                q = q.next
        if not p:
            s.next = q
        if not q:
            s.next = p
        return head_node
        
    def print_item(self):
        current_node = self.head
         
        while current_node:
            print(current_node.data, "-")
            current_node = current_node.next
    

if __name__ == "__main__":
    ls  = LinkedList()
   # ls.prepend(0)
    ls.append(1)
    ls.append(4)
    ls.append(7)
    ls.append(9)
#    ls.delete(-1)
#    ls.prepend(-1)
#    ls.delete(2)
    ls1 = LinkedList()
    ls1.append(2)
    ls1.append(3)
    ls1.append(6)
    ls.merge_list(ls1)
    ls.print_item()

 
        
        
        
        