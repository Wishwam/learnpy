# implementation of stack using list
stack = []
def push(value):
    stack.append(value)

def pop():
    if not stack:
        print("Stack Underflow")
    else:
        print("popped: ", stack.pop())

def peek():
    if not stack:
        print("Stack is empty")
    else:
        print("Top Element", stack[-1])

def traverse():
    if not stack:
        print("Stack is empty")
    else:
        print("Stack (Top to Bottom): ", stack[::-1])

def search(value):
    if value in stack:
        pos = len(stack) - stack[::-1].index(value) - 1
        print(f"{value} found at position {pos} (from bottom)")
    else:
        print(f"{value} not found in stack")

        

push(10)
push(20)
push(30)
traverse()
peek()
search(20)
pop()
traverse()
print("---------------------------------------")
# --------------------------
# infix to postfix conversion stack
def precedence(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    return 0

def infix_to_postfix(expression):
    result = "" 
    stack = []
    for char in expression:
        if char.isalnum():
         result += char
        elif char == '(':
         stack.append(char)
        elif char == ')':
         while stack and stack[-1] != '(':
            result += stack.pop()
         stack.pop()
        else:
          while stack and precedence(stack[-1]) >= precedence(char):
            result += stack.pop()
        stack.append(char)
    while stack:
        result += stack.pop()

    return result

expr = "A+B*(C-D)/E"
print("Infix : ", expr)
print("postfix:", infix_to_postfix(expr))
print("-------------------------------")
# ------------------
# postfix expression evaluation using stack
def evaluate_postfix(expression):
   stack = []
   for char in expression:
      if char.isdigit():
        stack.append(int(char))
      else:
        b = stack.pop()
        a = stack.pop()
        if char == '+':
            stack.append(a+b)
        elif char == '-':
           stack.append(a-b)
        elif char == '*':
           stack.append(a*b)
        elif char == '/':
           stack.append(a//b)
   return stack.pop()

expr = "53+62/*"
print("Postfix Expression: ", expr)
print("Evaluated Result: ", evaluate_postfix(expr))
# ------------------------------------------
print("-------------------------------------")
# queue implementation
class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None]*size
        self.front = -1
        self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def is_empty(self):
        return self.front == -1

    def enqueue(self, val):
        if self.is_full():
            print("Queue Overflow")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = val
        print(f"Enqueued: {val}")

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return
        val = self.queue[self.front]
        print(f"Dequeued: {val}")
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

    def traverse(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("Queue:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

    def search(self, key):
        if self.is_empty():
            print("Queue is empty")
            return
        i = self.front
        while True:
            if self.queue[i] == key:
                print(f"Element {key} found at position {i}")
                return
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print(f"Element {key} not found")

if __name__ == "__main__":
    q = Queue(5)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.traverse()
    q.dequeue()
    q.traverse()
    q.search(20)
    q.search(50)
# ---------------------
print("--------------------------------")
# singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        temp = self.head
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if not temp:
            print(f"Element {key} not found.")
            return
        if not prev:
            self.head = temp.next
        else:
            prev.next = temp.next
        print(f"Deleted: {key}")

    def traverse(self):
        temp = self.head
        print("List:", end=" ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                print(f"Element {key} found.")
                return
            temp = temp.next
        print(f"Element {key} not found.")

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev
        print("List reversed.")

if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_beginning(5)
    ll.traverse()
    ll.search(20)
    ll.delete_node(10)
    ll.traverse()
    ll.reverse()
    ll.traverse()