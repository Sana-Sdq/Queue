from collections import deque
import heapq


# 1. Queue Class
class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


# 2. Priority Queue Class
class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        heapq.heappush(self.queue, (-priority, item))

    def dequeue(self):
        if not self.is_empty():
            return heapq.heappop(self.queue)[1]
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


# 3. Circular Queue Class
class CircularQueue:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.front = self.rear = self.size = 0

    def enqueue(self, item):
        if self.size == self.max_size:
            raise Exception("Circular queue is full")
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.max_size
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Circular queue is empty")
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return item

    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size


# Maze Solver using Queue
def maze_solver(maze, start, end):
    q = Queue()
    q.enqueue((start, [start]))
    visited = set()

    while not q.is_empty():
        (current, path) = q.dequeue()
        if current == end:
            return path
        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_position = (current[0] + direction[0], current[1] + direction[1])
            if (
                    len(maze) > next_position[0] >= 0 == maze[next_position[0]][next_position[1]] and 0 <= next_position[1] < len(maze[0]) and next_position not in visited):
                q.enqueue((next_position, path + [next_position]))
                visited.add(next_position)
    return None


# Josephus Problem
def josephus(n, k):
    q = Queue()
    for i in range(1, n + 1):
        q.enqueue(i)

    while q.size() > 1:
        for _ in range(k - 1):
            q.enqueue(q.dequeue())
        q.dequeue()

    return q.dequeue()


# Which One
class AsciiPriorityQueue:
    def __init__(self, string):
        self.queue = PriorityQueue()
        for char in string:
            self.enqueue(char)

    def enqueue(self, item):
        self.queue.enqueue(item, ord(item))

    def dequeue(self):
        return self.queue.dequeue()

    def print_queue(self):
        items = sorted(self.queue.queue, key=lambda x: -x[0])
        print(', '.join(item[1] for item in items))

    def is_empty(self):
        return self.queue.is_empty()

    def size(self):
        return self.queue.size()


# Example usage
if __name__ == "__main__":
    # Maze Solver Example
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]
    start = (0, 0)
    end = (4, 4)
    print(maze_solver(maze, start, end))

    # Josephus Problem Example
    print(josephus(7, 3))

    # Which One Example
    string = "ARYAN"
    ascii_queue = AsciiPriorityQueue(string)
    ascii_queue.print_queue()
    print(ascii_queue.dequeue())
    ascii_queue.print_queue()
