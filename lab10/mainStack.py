from Stack import Stack
import os

def main():
    stack = Stack()
    stackFile = "inputStack.txt"
    if os.path.exists(stackFile):
        with open(stackFile) as file:
            for line in file:
                line = line.strip().split(" ")

                if line[0] == "push":
                    try:
                        stack.push(line[1])
                        print(f"Pushed {line[1]} to the stack")
                    except IndexError:
                        print("Error: No value to push!")

                elif line[0] == "pop":
                    try:
                        pop_val = stack.pop()
                        print(f"Popped {pop_val} off the stack")
                    except Exception as e:
                        print(f"Error: {e}")

                elif line[0] == "peek":
                    try:
                        peek_data = stack.peek()
                        print(f"Peeked {peek_data} at the top of stack")
                    except Exception as e:
                        print(f"Error: {e}")

                elif line[0] == "clear":
                    stack.clear()
                    print("Stack cleared")
                
                else:
                    print(stack)
    else:
        print(f"File '{stackFile}' not found!")

if __name__ == "__main__":
    main()