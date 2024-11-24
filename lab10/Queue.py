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

class EmptyQueueException(Exception):
    def __init__(self,action):
        self.__msg = "Queue is empty, action can't be completed!"
        super().__init__(self.__msg)

class Queue:
    def __init__(self):
        self.__head = None
        self.__tail = None

    # append data to queue (FIFO)
    def enqueue(self, data):
        new_node = Node(data)
        if self.__head is None:  # queue is empty
            self.__head = new_node
            self.__tail = new_node  # set tail to new node
        else:  # append to end of queue
            self.__tail.setNext(new_node)  # append new_node
            self.__tail = new_node  # update tail to new_node

    def dequeue(self):
        if self.__head is None: # queue empty
            raise EmptyQueueException("dequeue()")
        
        elif self.__head.getNext() is None: # only one element
            dequeue_data = self.__head.getData() # retain node's data
            self.__head, self.__tail = None, None # remove node, update stack
            return dequeue_data
        
        else: # 2 or more elements
            dequeue_data = self.__head.getData()
            self.__head = self.__head.getNext()
            return dequeue_data
        
    def peek(self):
        if self.__head == None: # empty queue
            raise EmptyQueueException("peek()")
        else:
            return self.__head.getData()
        
    def clear(self):
        # let garbage collection do the work
        self.__head, self.__tail = None, None

    def __str__(self) -> str:
        # empty queue
        if self.__head == None:
            return ""
        
        # return queue's data as string
        else:
            queue_str = "" # queue's data as string
            current = self.__head # temp ref for iteration
            while current is not None:
                if current.getNext() is None: # last element
                    queue_str += f"{current.getData()}"
                else:
                    queue_str += f"{current.getData()}, "
                current = current.getNext() # iterate

            return queue_str.rstrip(",")