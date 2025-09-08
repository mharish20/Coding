class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.size=0

    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node
        self.size+=1

    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        self.size+=1
    
    def insert_at_position(self,index,data):
        if index<0:
            print("Index must be greater than 0")
            return
        if index==0:
            self.prepend(data)
            return
        if index>self.size:
            self.append(data)
            return
        new_node=Node(data)
        current=self.head
        for i in range(index-1):
            current=current.next
        new_node.next=current.next
        current.next=new_node
        self.size+=1

    def reverse(self):
        prev=None
        current=self.head

        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        self.head=prev
    
    def display_reverse(self):
        stack=[]
        current=self.head
        while current:
            stack.append(current.data)
            current=current.next
        print("None",end='-->')
        while stack:
            print(stack.pop(),end='-->')
        print()

    def odd_or_even(self):
        flag=0
        current=self.head
        while current:
            flag= not flag
            current=current.next
        print("Odd") if flag==1 else print("Even") 
    
    def display(self):
        if not self.head:
            print("The list is Empty.")
            return
        print("Linked List:")
        current=self.head
        while current:
            print(current.data,end="-->")
            current=current.next
        print()

ll=LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)
ll.display_reverse()
ll.odd_or_even()
ll.display()