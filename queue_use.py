from queue_pynguin import Queue

# Create a new queue instance
my_queue = Queue()

# Add items to the queue
my_queue.enqueue("apple")
my_queue.enqueue("banana")
my_queue.enqueue("cherry")

# Check the size of the queue
print("Queue size:", my_queue.size())  # Output: Queue size: 3

# Get and remove the item at the front of the queue
print("Dequeued item:", my_queue.dequeue())  # Output: Dequeued item: apple

# Check the item at the front of the queue
print("Front item:", my_queue.peek())  # Output: Front item: banana
