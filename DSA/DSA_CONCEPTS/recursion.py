# ___ Factorial ___ 
# Time complexity: O(n)
# Space complexity: O(n)
def factorial(n):
    if n == 0:
        return 1
    
    return n * factorial(n-1)

f10 = factorial(10)
print(f10)

# ___ Fibanocci ___ 
# F(0) = 0, F(1)=1, if n> 1 -> F(n) = F(n-1) + F(n-2)
# Time complexity: O(2^n)
# Space complexity: O(n)
def fibanocci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibanocci(n-1) + fibanocci(n-2)

f5 = fibanocci(7)
print(f5)

# ___ Linked List ___
class SinglyNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)
    

head = SinglyNode(1)
A = SinglyNode(3)
B =  SinglyNode(5)
C = SinglyNode(7)

head.next = A
A.next = B
B.next = C

print(head)

# Time complexity: O(n)
# Space complexity: O(n)
def reverse(head):
    if not head:
        return 
    reverse(head.next)
    print(head)

reverse(head)

