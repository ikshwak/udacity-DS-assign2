class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        self.count += 1
            
    def dequeue(self):
        if self.count == 0:
            return None
        value = self.head.value
        self.head = self.head.next
        self.count -= 1
        return value

class LRU_Cache(object):

    def __init__(self, capacity):
        """
        1. the LRU cache class has:
            - a list to maintain keys in a Queue.
            - a dictionary to maintain the key/value pairs.
            - variables to maintain the cache size.
            - constants to maintain the cache capacicty.
        """
        self.keyList = Queue()
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
        value = self.cache.get(key)
        if value != None:
            return value
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
        if self.cacheSize >= self.capacity:
            cacheValPop = self.keyList.dequeue()
            if cacheValPop != None:
                self.cache.pop(cacheValPop)
        if self.cache.get(key) == None:
            self.keyList.enqueue(key)
        self.cache[key] = value
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

    print(our_cache)
    count = 0
    while count<=5:
        print(our_cache.get(count))
        count+=1


test_case1()
"""
{0: 0, 1: 1, 2: 2, 3: 3, 4: 4}
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
    2. sets the same key mulitple times
    3. get value will return the most recently set value
    4. please note: the keyList will not grow, it only has unique key list.
    """
    our_cache = LRU_Cache(5)
    count = 0
    while count<5:
        our_cache.set(1,count)
        count+=1

    print(our_cache.get(1))

test_case3()
"""
TEST CASE 3
4
"""
