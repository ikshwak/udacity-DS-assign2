import os

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
    fileList = []
    return find_files_help(suffix,path,fileList)

def find_files_help(suffix,path,fileList):
    if path == None or suffix == None:
        return None
    try:
        items = os.listdir(path)
    except FileNotFoundError:
        return None
    for item in items:
        localItem = os.path.join(path,item)
        if os.path.isdir(localItem):
            find_files_help(suffix,localItem,fileList)
        elif os.path.isfile(localItem) and localItem.endswith(suffix):
            fileList.append(localItem)
    return fileList

def test_function(casenum, suffix, path):
    print("TEST CASE "+str(casenum))
    fileList = find_files(suffix, path)
    if fileList is None or len(fileList) == 0:
        print("None")
        return    
    for item in fileList:
        print(item)

"""
TEST CASE 1
"""
test_function(1, ".c", "./testdir")
"""
./testdir\testdir\subdir1\a.c
./testdir\testdir\subdir3\subsubdir1\b.c
./testdir\testdir\subdir5\a.c
./testdir\testdir\t1.c
"""

"""
TEST CASE 2
"""
test_function(2, ".c", ".")
"""
.\testdir\testdir\subdir1\a.c
.\testdir\testdir\subdir3\subsubdir1\b.c
.\testdir\testdir\subdir5\a.c
.\testdir\testdir\t1.c
"""

"""
TEST CASE 3
"""
test_function(3, ". c", ".")
"""
None
"""

"""
TEST CASE 4
"""
test_function(4, ".c", "./nodir")
"""
None
"""
