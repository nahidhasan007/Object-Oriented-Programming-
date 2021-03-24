class Node:
    def __init__(self,data=None,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next
class DoublyList:
    count = 0
    def __init__(self):
        self.head = None

    def insert_sequentially(self,data):
        if self.head is None:
            self.head = Node(data,None,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,itr.prev,None)

    def insert_at_position(self,index,data):
        pos = 0
        if index<0:
            print("invalid Position")
        if index == 0:
            self.head = Node(data,None,self.head)
        itr = self.head
        while itr:
            if pos == index-1:
                itr.next = Node(data,itr,itr.next)
                break
            itr = itr.next
            pos+=1
    
    def PrintList(self):
        lst = []
        itr = self.head
        while itr:
            lst.append(itr.data)
            itr = itr.next
        print(lst)

dl = DoublyList()
dl.insert_sequentially(12)
dl.insert_sequentially(2)
dl.insert_sequentially(21)
dl.insert_at_position(0,267)
dl.insert_at_position(2,100)
dl.PrintList()
        