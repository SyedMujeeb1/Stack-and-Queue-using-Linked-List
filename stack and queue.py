class Node:
    """A simple Node class for the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    """Simplified Stack implementation using a linked list."""
    def __init__(self):
        self.top = None

    def push(self, data):
        """Add an item to the stack."""
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"Pushed {data}")

    def pop(self):
        """Remove the top item from the stack."""
        if self.top is None:
            print("Stack is empty")
            return None
        data = self.top.data
        self.top = self.top.next
        print(f"Popped {data}")
        return data


class Queue:
    """Simplified Queue implementation using a linked list."""
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        """Add an item to the queue."""
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"Enqueued {data}")

    def dequeue(self):
        """Remove the front item from the queue."""
        if self.front is None:
            print("Queue is empty")
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        print(f"Dequeued {data}")
        return data


# Testing the simplified implementation
if __name__ == "__main__":
    print("=== Stack Example ===")
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.pop()
    stack.pop()
    stack.pop()

    print("\n=== Queue Example ===")
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()