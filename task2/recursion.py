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
        localItem = path + "/" + item
        print("item " + localItem)
        if os.path.isdir(localItem):
            find_files(suffix,localItem)
        elif os.path.isfile(localItem) and localItem.endswith(suffix):
            print(".c file " + localItem)
            fileList.append(localItem)
    return fileList

print(find_files(".c", "./testdir"))

"""
# Let us print the files in the directory in which you are running this script
fileList = os.listdir("./testdir/testdir")
print (fileList)

for file in fileList:
    print(file)
    if os.path.isdir(os.path.join("./testdir/testdir", file)):
        print(os.listdir(os.path.join("./testdir/testdir", file)))

# Let us check if this file is indeed a file!
print (os.path.isfile("./recursion.py"))

print (os.path.isdir("./testdir"))

# Does the file end with .py?
print ("./ex.py".endswith(".py"))
"""
