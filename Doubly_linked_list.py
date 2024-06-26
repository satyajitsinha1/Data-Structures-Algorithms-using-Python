class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev = prev
        self.item = item
        self.next = next
        
class DLL:
    def __init__(self,start=None):
        self.start = start
        
    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self,item):
        n = Node(None,item,self.start)
        if not self.is_empty():
            self.start.prev = n
        self.start = n
            
    def insert_at_last(self,item):
        n = Node(None,item,None)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
            n.prev = temp
        else:
            self.start = n
            
    def search(self,item):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                if temp.item == item:
                    return temp
                temp = temp.next
        print("No data in the list")
        return None
    
    def insert_after(self,temp,item):
        if temp is not None:
            n = Node(temp,item,temp.next)
            if temp.next is not None:
                temp.next.prev = n
            temp.next = n
            print("Data Inserted")
        else:
            print("No such node to enter the data.")
            
    def print_list(self):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                print(temp.item,end=' ')
                temp = temp.next
            print()  
        else:
            print('List is empty nothing to print.')
         
    def delete_first(self):
        if not self.is_empty():
            if self.start.next is not None:
                self.start = self.start.next
                self.start.prev = None
            else:
                self.start = None
        else:
            print("Nothing to delete")
            
    def delete_last(self):
        if not self.is_empty():
            if self.start.next is not None:
                temp = self.start
                while temp.next is not None:
                    temp = temp.next
                temp.prev.next = None
            else:
                self.start = None        
        else:
            print("Nothing to delete")
    
    def delete_item(self, item):
        if not self.is_empty():
            temp = self.start
            if temp.item == item:
                self.delete_first()
                return
            while temp is not None:
                if temp.item == item:
                    if temp.next is None:
                        self.delete_last()
                    else:
                        temp.prev.next = temp.next 
                        temp.next.prev = temp.prev
                    return
                temp = temp.next
        else:
            print("Nothing to delete.")
    
    
mylist = DLL()
mylist.insert_at_start(1)
mylist.insert_at_last(2)
mylist.insert_after(mylist.search(2),3)
mylist.delete_item(1)
mylist.print_list()

    
    