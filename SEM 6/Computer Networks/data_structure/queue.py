"""1. enqueue(self, value):
Adds an element to the rear of the queue.
2. dequeue(self):
Removes and returns the element from the front of the queue.
Returns nil if the queue is empty.
3. front(self):
Returns the element at the front of the queue without removing it.
Returns nil if the queue is empty.
4. is_empty(self):
Checks whether the queue is empty.
Returns true if the queue is empty, otherwise false.
5. size(self):
Returns the current size (number of elements) of the queue.
6. display(self):
Displays the contents of the queue (usually for debugging purposes)."""


class Queue:
    def __init__(self):
        self.queue = []
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        if self.is_empty():
            return "stack is empty"
        return self.queue.pop(0)
    
    def front (self):
        return self.queue[0]
    
    def display(self):
        for i in range(len(self.queue)):
            print(self.queue[i], " -->", end="")
        print()
    
    
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.display()
queue.dequeue()
queue.display()
            
