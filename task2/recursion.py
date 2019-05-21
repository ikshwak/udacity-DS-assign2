import os

fileList = []
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if path == None or suffix == None:
        return None
    try:
        items = os.listdir(path)
    except FileNotFoundError:
        return None
    for item in items:
        localItem = os.path.join(path,item)
        if os.path.isdir(localItem):
            find_files(suffix,localItem)
        elif os.path.isfile(localItem) and localItem.endswith(suffix):
            fileList.append(localItem)
    return fileList


def test_function():
    find_files(".c", "./testdir")
    for item in fileList:
        print(item)

test_function()
