class Stack:
    def __init__(self):
        self.stack = []
    
    # Insert an element
    def push(self, ele):
        self.stack.append(ele)
        
    # Removing an element.
    def pop(self):
        # if self.is_empty():
        #     return "Stack is empty"
        assert(not self.is_empty())
        self.stack.pop()
        
    
    # Shows the top element.
    def top(self):
        # if self.is_empty():
        #     return "Stack is empty"
        assert(not self.is_empty())
        return self.stack[-1]
    
    # Check Stack is empty or not.
    def is_empty(self):
        return len(self.stack) == 0
       
    
    # Display the current state of stack.
    def display(self):
        for i in range(len(self.stack)):
            print(self.stack[i], "--> ", end="")
        print()
            

#####################################
stack = Stack()
stack.push(1)
stack.push(2)
stack.display()
stack.pop()
stack.display()
stack.pop()

