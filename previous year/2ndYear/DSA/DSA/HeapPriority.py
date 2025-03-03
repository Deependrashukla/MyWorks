class PriorityQueueBase:
    """Abstract base class for a priority queue."""

    class Item:
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key  

        def is_empty(self):  
            """Return True if the priority queue is empty."""
            return len(self) == 0

class HeapPriorityQueue(PriorityQueueBase):

    def is_empty(self):  
        """Return True if the priority queue is empty."""
        return len(self) == 0

    def parent(self, j):
        return (j - 1) // 2

    def left(self, j):
        return 2 * j + 1

    def right(self, j):
        return 2 * j + 2

    def has_left(self, j):
        return self.left(j) < len(self.data)  

    def has_right(self, j):
        return self.right(j) < len(self.data)  
    def swap(self, i, j):
        """Swap the elements at indices i and j of array."""
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def upheap(self, j):
        parent = self.parent(j)
        if j > 0 and self.data[j] < self.data[parent]:
            self.swap(j, parent)
            self.upheap(parent)  

    def downheap(self, j):
        if self.has_left(j):
            left = self.left(j)
            small_child = left  
            if self.has_right(j):
                right = self.right(j)
                if self.data[right] < self.data[left]:
                    small_child = right
            if self.data[small_child] < self.data[j]:
                self.swap(j, small_child)
                self.downheap(small_child)

    def __init__(self):
        """Create a new empty Priority Queue."""
        self.data = []

    def __len__(self):
        """
        Return the number of items in the priority queue.
        """
        return len(self.data)

    def add(self, key, value):
        """Add a key-value pair to the priority queue."""
        self.data.append(self.Item(key, value))
        self.upheap(len(self.data) - 1)  

    def min(self):
        """
        Return but do not remove (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty("Priority queue is empty.")
        item = self.data[0]
        return item._key, item._value

    def remove_min(self):
        """
        Remove and return (k,v) tuple with the minimum key.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty("Priority queue is empty.")
        self.swap(0, len(self.data) - 1)  
        item = self.data.pop()  
        self.downheap(0)
        return item._key, item._value


    def update_key(self, queue, new_key):
        for i, item in enumerate(self.data):
            if item._value[1] is queue:
                old_key = item._key
                item._key = new_key
                if new_key < old_key:
                    self.upheap(i)
                else:
                    self.downheap(i)
                return
        raise ValueError("Queue not found in the priority queue.")
