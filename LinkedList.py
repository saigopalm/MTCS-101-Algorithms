'''
Program to perform constant time deletion in a linked list
Author: Mantha Sai Gopal
Reg.no: 23358
'''

class Node(object):
    def __init__(self, value:int):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.length = 0

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = Node(new_element)
        else:
            self.head = Node(new_element)
        self.length += 1

    def get_position(self, position):
        if position < 0 or position >= self.length:
            print("Invalid position!")
            return None

        counter = 0
        current = self.head

        while current:
            if counter == position:
                return current
            else:
                current = current.next
                counter += 1

        print("Invalid position!")
        return None

    def insert(self, new_element, position):
        if position < 1 or position > self.length + 1:
            print("Invalid position")
            return
        
        counter = 1
        current = self.head
        if position == 1:
            new_element.next = self.head.next
            self.head = new_element
        else:
            if self.length >= position :
                while current:
                    if counter == position-1:
                        new_element.next = current.next
                        current.next = new_element
                        break
                    else:
                        current = current.next
                        counter += 1
        self.length += 1

    def delete(self, value):
        if not self.head :
            return None
        current = self.head
        if current.value == value:
            self.head = current.next
            self.length -= 1
        else:
            while current.next:
                if current.next.value == value:
                    current.next = current.next.next
                    self.length -= 1
                    break
                current = current.next

    def getPtr(self, position):
        if position < 0 or position >= self.length or not self.head:
            print("Invalid position")
            return None

        counter = 0
        current = self.head

        while current:
            if counter == position:
                return id(current)
            current = current.next
            counter += 1

    def delPtrElement(self, pointer):
        if self.length == 0 or not self.head:
            print("Linked list is empty :)")
            return

        if not pointer.next:
            print("Inserting -∞ at the last node.")
            pointer.value = float("-inf")
            self.length -= 1
            return

        # Copy the value from the next node to the current node
        pointer.value = pointer.next.value

        # Performing deletion by dropping the next element
        pointer.next = pointer.next.next

        self.length -= 1

    def insertPointer(self, pointer, newElement):

        if not pointer:
            print("Location not correct")
            return

        newNode = Node(newElement)
        newNode.next=pointer.next
        pointer.next = newNode
        self.length += 1

    def printLinkedList(self):
        current = self.head
        while current:
            next_node = current.next
            if next_node:
                arrow = " --> "
            else:
                arrow = " --> None"
            print(f"{current.value}{arrow}",end='')
            current = next_node
        print('\n')

    def len(self):
        return self.length  


# Test cases
linked_list = LinkedList()
for i in range(5):
    linked_list.append(i)

linked_list.printLinkedList()
print("Length: {}\n".format(linked_list.len()))

# Obtaining the index
ptr1 = linked_list.get_position(2)

linked_list.insertPointer(ptr1,22)
linked_list.printLinkedList()
print(f"Length: {linked_list.len()}\n")

linked_list.delPtrElement(ptr1)
linked_list.printLinkedList()
print(f"Length: {linked_list.len()}\n")

ptr2 = linked_list.get_position(1)
linked_list.delPtrElement(ptr2)
linked_list.printLinkedList()
print(f"Length: {linked_list.len()}\n")