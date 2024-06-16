class Node:
    def __init__ (self,data=None,next=None):
        self.data=data
        self.next = next
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0
        
    def print_queue(self):
        if self.is_empty():
            print("No Data in the Queue.")
        else:
            temp = self.front
            while temp is not None:
                print(temp.data,end=" ")
                temp = temp.next
        print()
            
    
    def is_empty(self):
        return self.front == None
    
    def enqueue(self,data):
        n = Node(data)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n    
        self.count += 1
        
    def dequeue(self):
        if self.is_empty():
            print('Empty QUEUE')
        elif self.front== self.rear:
            self.front= None
            self.rear=None
            self.count-=1
        else:
            self.front=self.front.next
            self.count-=1
            
    def get_front(self):
        if not self.is_empty():
            return self.front.data
        else:
            print("NO DATA IN THE QUEUE")
        
    def get_rear(self):
        if self.is_empty():
            print("NO DATA IN THE QUEUE")
        else:
            return self.rear.data  
        
    def size(self):
        return self.count
    
# q1= Queue()
# q1.enqueue(10)
# q1.enqueue(30)
# q1.enqueue(40)
# q1.enqueue(50)
# q1.print_queue()
# print('Front: ', q1.get_front(), 'End: ', q1.get_rear())
# q1.dequeue()
# print('Front: ', q1.get_front(), 'End: ', q1.get_rear())
# print(q1.size())
# q1.print_queue()
    