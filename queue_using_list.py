class Queue:
    
    def __init__(self):
        self.myqueue = []
    
    
    def is_empty(self):
        return len(self.myqueue) == 0
    
    
    def enqueue(self,data):
        self.myqueue.insert(0,data)
        
        
    def print_queue(self):
        if not self.is_empty():
            for i in reversed(self.myqueue):
                print(i,end=" ")   
        else:
            raise IndexError("Empty Queue")
        print() 
            
            
    def dequeue(self):
        if not self.is_empty():
            return self.myqueue.pop(-1) 
        else:
            raise IndexError("No data in the Queue")
    
    
    def get_front(self):
        if not self.is_empty():
            return self.myqueue[-1]
        else:
            raise IndexError("No data in the Queue")
    
    
    def get_rear(self):
        if not self.is_empty():
            return self.myqueue[0]
    
    
    def size(self):
        return len(self.myqueue)
    

# a = Queue()
# a.enqueue(1)
# a.enqueue(2)
# a.enqueue(3)
# a.enqueue(4)
# a.enqueue(5)
# a.dequeue()
# a.dequeue()
# a.enqueue(6)
# a.print_queue()
# print('Front Element: ',a.get_front())
# print('Rear Element: ',a.get_rear())
# print('Size: ',a.size())
