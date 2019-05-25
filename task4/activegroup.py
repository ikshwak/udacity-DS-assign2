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


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
child.add_user("test")
child.add_group(sub_child)
parent.add_group(child)



def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    userSet = set()
    create_user_set(group, userSet)
    print(userSet)
    if user in userSet:
        return True
    return False

def create_user_set(group, userSet):
    if group == None:
        return
    groupList = group.get_groups()
    if len(groupList) == 0:
        return
    for gr in groupList:
        create_user_set(gr, userSet)
        for user in gr.get_users():
            userSet.add(user)


if is_user_in_group("test", parent) == True:
    print("test in parent group")
else:
    print("test not in parent group")
