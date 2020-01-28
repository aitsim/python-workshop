# linked liste used a nodes
# head ---> node1----> node2----> null
# double linked liste
#  head ---> <---- node .....



class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node

    def delete(self,element):
        cur = self.head

        if cur.next.data==element:
            cur.next=cur.next.next

    def lenght(self):
        i=0
        cur=self.head
        while cur.next!=None:
            i = i+1
            cur = cur.next
        return i

    def display(self):
        tab = []
        cur=self.head
        while cur.next != None:
            cur = cur.next
            tab.append(cur.data)
        print(tab)



    def get(self,index):
        i=0
        cur=self.head
        while i< self.lenght():
            cur = cur.next
            if i == index:
                return cur.data
            i = i + 1

    # failed
    def delete(self, index):

        i = 0
        cur = self.head
        cur_next = cur.next
        while i < self.lenght():
            if i == index:
                    cur.next = cur_next.next
            else:
                cur=cur.next
                cur_next=cur_next.next

                i = i+1
            return






mylist = LinkedList()

mylist.append(9)
mylist.append(8)
mylist.append(7)
mylist.append(6)


mylist.display()

print(mylist.get(2))

mylist.delete(1)
mylist.display()








