class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class SinglyList:
    count = 0
    def __init__(self):
        self.head = None

    def insert_beg(self,data):
        node = Node(data,self.head)
        self.head = node
        self.count +=1

    def insert_end(self,data):
        if self.head is None:
            node = Node(data,self.head)
            self.count+=1
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
        self.count+=1

    def insert_at(self,index,data):
        if index<0:
            print("Invalid Index")
        if index==0:
            self.head = Node(data,self.head)
            self.count+=1
        pos = 0
        itr = self.head
        while itr:
            if pos == index-1:
                node = Node(data,itr.next)
                itr.next = node
                self.count+=1
                break
            itr = itr.next
            pos+=1
    def delete_at(self,index):
        pos = 0
        itr = self.head
        if index==0:
            self.head = itr.next
        while itr:
            if pos == index-1:
                itr.next = itr.next.next
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

l1 = SinglyList()
l1.insert_beg(3)
l1.insert_beg(34)
l1.insert_beg(56)
l1.insert_beg(6)
l1.insert_end(12)
l1.insert_at(0,11)
l1.insert_at(2,123)
l1.delete_at(0)
l1.delete_at(2)
print(l1.count)
print(l1.PrintList())