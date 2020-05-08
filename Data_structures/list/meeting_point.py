class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        
    def push(self,data):
        new_node = Node(data)
        if(self.head == None):
            self.head = new_node
            return
        temp = self.head
        while temp.next!=None:
            temp = temp.next
        temp.next = new_node

    def input_push(self,l):
        for i in l:
            self.push(i)

    def display(self):
        temp = self.head
        print('-----------')
        while temp:
            print(temp.data)
            temp = temp.next        

def meeting_point(l1,l2):
    temp1 = l1.head
    while temp1:
        temp2 = l2.head
        while temp2:
            if temp1.data == temp2.data:
                t1 = temp1
                t2 = temp2
                f=0
                while t2!=None and t1!=None:
                    if t1.data == t2.data:
                        f = 1
                    else:
                        f = 0
                        break
                    t1 = t1.next
                    t2 = t2.next
                if f == 1 :
                    print('Meeting point: ',temp1.data)
                    return
            temp2 = temp2.next
        temp1 = temp1.next
    print('No meeting point')
    
lst1 = LinkedList()
lst2 = LinkedList()
lst1.input_push(list(map(int,input().split())))
lst2.input_push(list(map(int,input().split())))
lst1.display()
lst2.display()
meeting_point(lst1,lst2)

