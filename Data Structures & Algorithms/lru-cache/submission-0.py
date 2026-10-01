class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None

    def move_to_head(self, node):
        if node is self.head:
            return

        prev_node = node.prev
        next_node = node.next

        if prev_node:
            prev_node.next = next_node

        if next_node:
            next_node.prev = prev_node

        if node is self.tail:
            self.tail = prev_node

        node.prev = None
        node.next = self.head

        if self.head:
            self.head.prev = node
        else:
            self.tail = node

        self.head = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)
            return
        
        node = Node(key, value)

        node.prev = None
        node.next = self.head

        if self.head:
            self.head.prev = node
        else:
            self.tail = node

        self.head = node
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            lru_nodes = self.tail

            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
            
            del self.cache[lru_nodes.key]
        
























