"""LRU Cache implementation"""
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.dic = dict()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key):
        if key in self.dic:
            node = self.dic[key]
            self._remove(node)
            self._add(node)
            val = node.val
            return val
        return -1
    
    
    def set(self, key, value):
        node = Node(key, value)
        if key in self.dic:
            self._remove(self.dic[key])
        self.dic[key] = node
        self._add(node)
        # check capactiy of cache
        if len(self.dic) > self.capacity:
            first_node = self.head.next
            self._remove(first_node)
            del self.dic[first_node.key]    


    def _remove(self, node):
        next_node = node.next
        prev_node = node.prev
        next_node.prev = prev_node
        prev_node.next = next_node
    
    def _add(self, node):
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

if __name__ == "__main__":
    LRU_CACHE = LRU(3)
    print(LRU_CACHE.get(1))
    print(LRU_CACHE.set(1, 1))
    print(LRU_CACHE.get(1))
    print(LRU_CACHE.set(2, 2))
    print(LRU_CACHE.set(3, 3))
    print(LRU_CACHE.get(3))
    print(LRU_CACHE.set(4, 4))
    print(LRU_CACHE.get(4))
    print(LRU_CACHE.get(1))
    print(LRU_CACHE.head.next.next.next.val)
    



