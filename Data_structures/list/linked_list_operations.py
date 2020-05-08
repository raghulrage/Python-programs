#create node attributes
class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

#linked list
class LinkedList:
    def __init__(self):
        self.head = None

    #add node
    def push(self,data):
        if(self.head == None):
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next:
                temp=temp.next
            temp.next = Node(data)

    #display linked list
    def display(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

    #find length of list
    def length(self):
        temp = self.head
        count = 0
        while temp:
            count+=1
            temp = temp.next
        return count

    #insert data
    def insert_middle(self,data,pos):
        temp = self.head
        new_node = Node(data)
        if temp.data == pos:
            new_node.next = self.head
            self.head = new_node
            return True
        prev = temp
        while True:
            if temp.data == pos:
                prev.next = new_node
                new_node.next = temp
                return True
            prev = temp
            temp = temp.next
            if temp == None:
                return False

    #delete node
    def delete_node(self,val):
        temp = self.head
        if val == temp.data:
            self.head = temp.next
            temp = None
            return True
        prev = temp
        while True:
            if(temp.data == val):
                prev.next = temp.next
                temp = None
                return True
            prev = temp
            temp = temp.next
            if(temp == None):
                return False

    #sort linked list
    def sorting(self):
        brk = self.length()
        while True:
            temp = self.head
            nxt  = temp.next
            count,flag = 1,0
            while True:
                count+=1
                if (temp.data>nxt.data):
                    nxt.data,temp.data = temp.data,nxt.data
                    flag = 1
                temp = temp.next
                nxt = nxt.next
                if count == brk:
                    break
            if flag == 0:
                break


while True:

    option = int(input('\n1.Create Linked List \n2.Insert data \n3.Delete data \n4.Display \n5.sort \n6.Exit\n'))
    try:
        if(option == 1):
            lst = LinkedList()
            for i in range(int(input('Enter length of list: '))):
                lst.push(int(input('Enter data: ')))

        elif(option == 2):
                val = int(input('Enter data to insert: '))
                pos = int(input('Enter data next to be inserted: '))
                if(lst.insert_middle(val,pos)):
                    print("\n**********After insertion**********")
                    lst.display()
                else:
                    print('Data not found')

        elif(option == 3):
                pos = int(input('Enter data to delete: '))
                if(lst.delete_node(pos)):
                    print('\n**********After Deletion**********')
                    lst.display()
                else:
                    print('Invalid input')

        elif(option == 4):
            print('\n**********Linked list**********')
            lst.display()

        elif(option == 5):
            lst.sorting()
            print('\n**********After sorting**********')
            lst.display()
        else:
            print('\n**********Thank you**********')
            break

    except NameError:
        print('\n**********Please create linked list first**********')
