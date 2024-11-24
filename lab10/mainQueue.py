from Queue import Queue
import os

def main():
    queue = Queue()
    queueFile = "inputQueue.txt"
    if os.path.exists(queueFile):
        with open(queueFile) as file:
            for line in file:
                line = line.strip().split(" ")

                if line[0] == "enqueue":
                    try:
                        queue.enqueue(line[1])
                        print(f"Enqueued {line[1]} to the queue")
                    except IndexError:
                        print("Error: No value to push!")

                elif line[0] == "dequeue":
                    try:
                        pop_val = queue.dequeue()
                        print(f"Dequeued {pop_val} from the queue")
                    except Exception as e:
                        print(f"Error: {e}")

                elif line[0] == "peek":
                    try:
                        peek_data = queue.peek()
                        print(f"Peeked {peek_data} at the front of the queue")
                    except Exception as e:
                        print(f"Error: {e}")

                elif line[0] == "clear":
                    queue.clear()
                    print("Queue cleared")
                
                else:
                    print(queue)
    else:
        print(f"File '{queueFile}' not found!")

if __name__ == "__main__":
    main()