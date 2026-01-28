# _________ STACKS - LIFO -> Bus ingress/ egress _________ 
stk = []
print(stk)

# Append to top of stack - O(1)
stk.append(1)
stk.append(2)
stk.append(3)
print(stk)

# Pop from stack - O(1)
if stk: #IsEmpty
    print(stk.pop())

# Peek - Ask whats on the top of the stack - O(1)
print(stk[-1])


# _________ Queues - FIFO -> shop queue _________
from collections import deque # double ended queue -> pop and append from the first and last (both ends)
q = deque()
print(q)

# Enque - add some element to the queue - O(1)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)
print(q)

# Deque (pop left) - pop the element from the left of the queue - O(1)
el1 = q.popleft()
print(el1)

#  pop from right - O(1)
el2 = q.pop()
print(el2)

# Peek from left - O(1)
if q:
    print(q[0])

# Peek from right - O(1)
if q:
    print(q[-1])