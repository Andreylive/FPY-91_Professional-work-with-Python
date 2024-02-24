class Stack:
    """Class for function: check balance"""
    def __init__(self):
        """init function to check balance"""
        self.stack = []

    def is_empty(self):
        """function to check if stack is empty"""
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, new_element):
        """function to add element in stack"""
        self.stack.append(new_element)

    def pop(self):
        """function pop element from a stack"""
        return self.stack.pop()

    def peek(self):
        """function to return last element in a stack"""
        return self.stack[-1]

    def size(self):
        """function to check lenth of the stack"""
        return len(self.stack)
