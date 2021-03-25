from doublylinkedlist import DoublyList

class Stack:
    def __init__(self):
        self.list = DoublyList()
    
    def Push(self,data):
        self.list.insert_sequentially(data)

    def Pop(self):
        self.list.delete_end()

    def Showlist(self):
        self.list.PrintList()

class Queue:
    def __init__(self):
        self.list = DoublyList()

    def In(self,data):
        self.list.insert_sequentially(data)
    
    def Out(self):
        self.list.delete_front()

    def Showlist(self):
        self.list.PrintList()

print("stack test")
s1 = Stack()
s1.Push(23)
s1.Push(12)
s1.Push(56)
s1.Showlist()
s1.Pop()
s1.Showlist()

print("queue test")
Q1 = Queue()
Q1.In(100)
Q1.In(200)
Q1.In(300)
Q1.Showlist()
Q1.Out()
Q1.Showlist()

