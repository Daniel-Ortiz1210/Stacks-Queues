
class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class NodeBasedQueue:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.count = 0
    

    def add(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.count += 1

    def quit(self):
        
        if self.count <= 1:
            self.head = None
            self.tail = None
        else:
            second = self.head.next
            second.prev = None
            self.head = second
        
        self.count -= 1

    def print_queue(self):

        current = self.tail

        while current != None:
            print(current.data)
            current = current.prev
        

q = NodeBasedQueue()
q.add("A")
q.add("B")
q.add("C")

q.quit()
q.print_queue()

            
