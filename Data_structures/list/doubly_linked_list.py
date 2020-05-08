class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinked:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self,data):
        new_node = Node(data)
        if self.head == None :
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        self.tail = new_node
        return



dlist = DoublyLinked()
dlist.push(1)
dlist.push(5)
dlist.push(4)
temp = dlist.head
while temp:
    print(temp.data)
    temp = temp.next
    
temp = dlist.tail
while temp:
    print(temp.data)
    temp = temp.prev
