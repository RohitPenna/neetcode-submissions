class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mapp = {}

        self.left = Node()
        self.right = Node()

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        nex = node.next

        prev.next = nex
        nex.prev = prev

    def insert(self, node):
        prev = self.right.prev

        prev.next = node
        node.prev = prev

        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.mapp:
            return -1

        node = self.mapp[key]

        self.remove(node)
        self.insert(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.mapp:
            self.remove(self.mapp[key])

        node = Node(key, value)
        self.mapp[key] = node
        self.insert(node)

        if len(self.mapp) > self.capacity:
            lru = self.left.next

            self.remove(lru)
            del self.mapp[lru.key]