class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

########################################################################################
######################     SOLUTION    #################################################
########################################################################################
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    userSet = set()
    create_user_set(group, userSet)
    if user in userSet:
        return True
    return False

def create_user_set(group, userSet):
    if group == None:
        return
    for user in group.get_users():
        userSet.add(user)
    groupList = group.get_groups()
    if len(groupList) == 0:
        return
    for gr in groupList:
        create_user_set(gr, userSet)

########################################################################################

def test_function(username, group):
    if is_user_in_group(username, group) == True:
        print(username + " in passed group")
    else:
        print(username + " not in passed group")


"""
TEST DATA
"""
parent = Group("parent")
parent.add_user("user")

child1 = Group("child1")
count = 0
while count <= 20:
    username = "user"+str(count)
    child1.add_user(username)
    count +=1
parent.add_group(child1)

sub_child1 = Group("subchild1")
while count <= 40:
    username = "user"+str(count)
    sub_child1.add_user(username)
    count +=1
child1.add_group(sub_child1)

child2 = Group("child2")
while count <= 60:
    username = "user"+str(count)
    child2.add_user(username)
    count +=1

parent.add_group(child2)

sub_child2 = Group("subchild2")
while count <= 80:
    username = "user"+str(count)
    sub_child2.add_user(username)
    count +=1
child2.add_group(sub_child2)


def test_case1():
    print("TEST CASE 1")
    test_function("user20", parent)
"""
"""

def test_case2():
    print("TEST CASE 2")
    test_function("user199", parent)
"""
"""

def test_case3():
    print("TEST CASE 3")
    test_function("user20", child1)
"""
"""

test_case1()
test_case2()
test_case3()
