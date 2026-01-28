# ____________________________________ Single linked list ______________________________________________________

class LinkedList:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return (str(self.val))


head = LinkedList(1)
el2 = LinkedList(2)
el3 = LinkedList(3)

head.next = el2
el2.next = el3

# Traverse the list - O(n)
def traverse(head):
    current = head
    while current:
        print(current.val)
        current = current.next
traverse(head)

# Display linked list - O(n)
def display(head):
    current = head
    elements = []
    while current:
        elements.append(str(current.val))
        current = current.next
    print(' -> '.join(elements))

display(head)

# Search for node value - O(n)
def search_node(head, target):
    current = head

    while current:
        if current.val  == target:
            return True
        current = current.next
    return False

print(search_node(head, 10))



# ____________________________________ Double linked list ______________________________________________________

class DoublyLinkedList:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.val)



head = tail = DoublyLinkedList(1)

def display(head):
    current = head
    elements = []
    while current:
        elements.append(str(current.val))
        current = current.next
    print(" <-> ".join(elements))

display(head)


def inset_at_beggining(head, tail, val):
    new_node = DoublyLinkedList(val, next=head)
    head.prev = new_node
    return new_node, tail
head, tail = inset_at_beggining(head, tail, 10)
display(head)


def insert_at_end(head, tail, val):
    new_node = DoublyLinkedList(val, prev=tail)
    tail.next = new_node
    return new_node, head

insert_at_end(head, tail, 20)
display(head)

