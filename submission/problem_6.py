class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value)
            cur_head = cur_head.next
            if cur_head:
                out_string += " -> "
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

########################################################################################
######################     SOLUTION    #################################################
########################################################################################
def union(llist_1, llist_2):
    if not llist_1 and not llist_2:
        return None
    if llist_1 and not llist_2:
        return llist_1
    if not llist_1 and llist_2:
        return llist_2

    unionSet = set()
    listIter = llist_1.head
    while listIter:
        unionSet.add(listIter.value)
        listIter = listIter.next

    listIter = llist_2.head
    while listIter:
        unionSet.add(listIter.value)
        listIter = listIter.next

    unionList = LinkedList()
    for item in unionSet:
        unionList.append(item)

    if unionList.size() > 0:
        return unionList
    else:
        return None

def intersection(llist_1, llist_2):
    if not llist_1:
        return None
    if not llist_2:
        return None

    ll_1_Dict = {}
    listIter = llist_1.head
    while listIter:
        ll_1_Dict[listIter.value] = 1
        listIter = listIter.next

    intersectSet = set()
    listIter = llist_2.head
    while listIter:
        if ll_1_Dict.get(listIter.value) == 1:
            intersectSet.add(listIter.value)
        listIter = listIter.next

    intersectList = LinkedList()
    for item in intersectSet:
        intersectList.append(item)

    if intersectList.size() > 0:
        return intersectList
    else:
        return None
########################################################################################


# Test case 1
print("TEST CASE 1")
ll_1 = LinkedList()
ll_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    ll_1.append(i)

for i in element_2:
    ll_2.append(i)

print (union(ll_1,ll_2))
print (intersection(ll_1,ll_2))

# Test case 2

print("TEST CASE 2")
ll_3 = LinkedList()
ll_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = []

for i in element_1:
    ll_3.append(i)

for i in element_2:
    ll_4.append(i)

print (union(ll_3,ll_4))
print (intersection(ll_3,ll_4))

# Test case 3

print("TEST CASE 3")
ll_5 = LinkedList()
ll_6 = LinkedList()

element_1 = []
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    ll_5.append(i)

for i in element_2:
    ll_6.append(i)

print (union(ll_5,ll_6))
print (intersection(ll_5,ll_6))
