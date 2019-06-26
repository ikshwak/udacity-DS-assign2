class Node:
    def __init__(self,key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

class keyList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        
    def addNode(self, node):
        new_node = node
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
        self.count += 1
            
    def removeNode(self, node):
        if self.count == 0 or node == None:
            return None

        if node.next:
            node.next.previous = node.previous

        if node.previous:
            node.previous.next = node.next
        
        if not node.next and not node.previous:
            self.head = None
            self.tail = None

        if self.tail == node:
            self.tail = node.previous
            self.tail.next = None

        self.count -= 1
        return node

class LRU_Cache(object):

    def __init__(self, capacity):
        """
        1. the LRU cache class has:
            - a list to maintain keys in a Queue.
            - a dictionary to maintain the key/value pairs.
            - variables to maintain the cache size.
            - constants to maintain the cache capacicty.
        """
        self.keyList = keyList()
        self.cache = {}
        self.capacity = capacity
        self.cacheSize = 0

    def __str__(self):
        return str(self.cache)

    def get(self, key):
        """
        Get function returns the value of a key
        mapped to the cache(dictionary) maintained
        in the class. if there is no key/value pair
        it returns -1
        """
        node = self.cache.get(key)
        if node != None:
            new_node = self.keyList.removeNode(node)
            self.keyList.addNode(new_node)
            return node.value
        return -1

    def set(self, key, value):
        """
        set function adds the key/value pair to the cache(dictionary)
        in addition to that we also maintain a queue unique keys.
        If the cache size equals cache capacity we dequeue a key from our keyList
        and pop the corresponding key from the cache.
        the keyList is a FIFO so the last added key/value will be discarded from
        the cache and a new key/value pair will be accepted to maintain the cache size.
        """
        if self.capacity == 0:
            print("cannot set!! cache size is zero")
            return

        if self.cache.get(key) == None:
            new_node = Node(key,value)
            if self.cacheSize >= self.capacity:
                cacheValPop = self.keyList.removeNode(self.keyList.tail)
                if cacheValPop != None:
                    del self.cache[cacheValPop.key]
                    self.cacheSize -= 1
            self.cache[key] = new_node
            self.keyList.addNode(new_node)

        else:
            node = self.cache.get(key)
            node.value = value
            new_node = self.keyList.removeNode(node)
            self.keyList.addNode(new_node)

        self.cacheSize+=1


def test_case1():
    print("TEST CASE 1")
    """
    1. create a cache size of 5
    2. add 5 uniques key/value pairs
    3. get the corresponding key/value pairs
    4. one corner case to get a key not added to the cache 
    """
    our_cache = LRU_Cache(5)
    count = 0
    while count<5:
        our_cache.set(count,count)
        count+=1

    count = 0
    while count<=5:
        print(our_cache.get(count))
        count+=1


test_case1()
"""
0
1
2
3
4
-1
"""

def test_case2():
    print("TEST CASE 2")
    """
    1. create a cache of size 0
    2. try to set/get key/values
    """
    our_cache = LRU_Cache(0)
    our_cache.set(1,1)
    print(our_cache.get(1))

test_case2()
"""
cannot set!! cache size is zero
-1
"""

def test_case3():
    print("TEST CASE 3")
    """
    1. create a cache of size 5
    2. sets multiple keys larger than than the LRU capacity
    3. get value will return the most recently set value
    4. Least used item will deleted to accomodate new key/value pairs
    """
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)


    print(our_cache.get(1))       # returns 1
    print(our_cache.get(2))       # returns 2
    print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    print(our_cache.get(3))     # returns -1 because 3 is deleted from the cache as it is least recently used
    print(our_cache.get(4))     # returns 4
    our_cache.set(7, 7)
    print(our_cache.get(4))     # returns 4 as the previous get updates the position in the LRU list
    print(our_cache.get(1))     # returns -1 because 1 is deleted from the cache as it is least recently used
    print(our_cache.get(6))     # returns 6
    print(our_cache.get(7))     # returns 7


test_case3()
"""
TEST CASE 3
1
2
-1
-1
4
4
-1
6
7
"""
