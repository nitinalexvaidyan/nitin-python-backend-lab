# Binary Trees

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)
    
#                 1
#            2           3
#         4     5       10
# 
A=TreeNode(1)
B=TreeNode(2)
C=TreeNode(3)
D=TreeNode(4)
E=TreeNode(5)
F=TreeNode(10)

A.left=B
A.right=C
B.left=D
B.right=E 
C.left=F

# print(A)

# Recursive pre order traversal: Time complexity: O(n), Space Complexity: O(n)
def pre_order_traversal(node):
    if not node:
        return
    
    print(node)
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)

print("-----Pre Order traversal -----") 
pre_order_traversal(A)


# Recursive in order traversal: Time complexity: O(n), Space Complexity: O(n)
def in_order_traversal(node):
    if not node:
        return
    
    in_order_traversal(node.left)
    print(node)
    in_order_traversal(node.right)

print("----- In Order traversal -----")    
in_order_traversal(A)


# Recursive post order traversal: Time complexity: O(n), Space Complexity: O(n)
def post_order_traversal(node):
    if not node:
        return
    
    post_order_traversal(node.left)
    post_order_traversal(node.right)
    print(node)

print("----- Post Order traversal -----")    
post_order_traversal(A)


# Iterative  Pre order travesal (DFS) -> stacks Time:Time complexity: O(n), Space Complexity: O(n)
def pre_order_iterative(node):
    stack = [node]
    while stack:
        node = stack.pop()
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
        print(node)

print("----- Post Order iterative stack -----") 
pre_order_iterative(A)


# Level order traversal (BFS) -> queues, Time complexity: O(n), Space Complexity: O(n)
from collections import deque
def level_order_traversal(node):
    q = deque()
    q.append(node)
    while q:
        node = q.popleft()
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
        print(node)

print("_____ Level order traversal _____")
level_order_traversal(A)

# DFS Search
def search(node, target):
    if not node:
        return False
    
    if node.val == target:
        return True

    return search(node.left, target) or search(node.right, target)
print("DFS Search", search(A, 11))

# Binary search trees
#                     5
#             1             8
#         -1    3       7     9
# 

A2 = TreeNode(5)
B2 = TreeNode(1)
C2 = TreeNode(8)
D2 = TreeNode(-1)
E2 = TreeNode(3)
F2 = TreeNode(7)
G2 = TreeNode(9)

A2.left , A2.right = B2, C2
B2.left, B2.right = D2, E2
C2.left, C2.right = F2, G2

# DFS on BST, Time: O(log n), space: O(log n)
def search_bst(node, target):
    if not node:
        return False
    
    if node.val == target:
        return True
    
    if node.val > target:
        return search_bst(node.left, target)
    else:
        return search_bst(node.right, target)

print("Search BST", search_bst(A2, -11))