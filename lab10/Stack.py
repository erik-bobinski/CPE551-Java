class Node:
    def __init__(self,data):
        self.__data = data
        self.__next = None

    def getData(self):
        return self.__data
    
    def setData(self,data):
        self.__data = data

    def getNext(self):
        return self.__next

    def setNext(self,next):
        self.__next = next

class EmptyStackException(Exception):
    def __init__(self,action):
        self.__msg = "Stack is empty, action can't be completed!"
        super().__init__(self.__msg)

class Stack:
    def __init__(self):
        self.__head = None

    # prepend data to stack (LIFO)
    def push(self, data):
        temp = self.__head
        self.__head = Node(data)
        self.__head.setNext(temp)

    def pop(self):
        # check if stack is empty
        if self.__head == None:
            raise EmptyStackException("pop()")
        
        # return node's data
        else:
            popped_data = self.__head.getData() # retain node's data
            self.__head = self.__head.getNext() # remove node, update stack
            return popped_data
        
    def peek(self):
        # check if stack is empty
        if self.__head == None:
            raise EmptyStackException("peek()")
        
        # return node's data
        else:
            return self.__head.getData()
        
    def clear(self):
        # let garbage collection do the work
        self.__head = None

    def __str__(self) -> str:
        # empty stack
        if self.__head == None:
            return ""
        
        # return stack's data as string
        else:
            stack_str = "" # stack's data as string
            current = self.__head # temp ref for iteration
            while current is not None:
                if current.getNext() is None: # omit comma for last element
                    stack_str += f"{current.getData()}"
                else:
                    stack_str += f"{current.getData()}, "
                current = current.getNext() # iterate

            return stack_str.rstrip(",")