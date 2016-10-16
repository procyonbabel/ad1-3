# For compatability between Python versions 2.x and 3.x
# For all versions, print function should be in the same form: e.g. print(0)
from __future__ import print_function
# Name 1: Caroline Appleby
# Name 2: Chiao-ting Fang
# Name 3: Linjing Fu


# Create empty tree
def emptytree():
    return None


# Insert x into tree t
def insert(t, x):
    if t is None:
        return x, None, None
    else:
        key, left, right = t
        if x == key:
            return key, left, right
        elif x < key:
            return key, insert(left, x), right
        else:
            return key, left, insert(right, x)


# Create tree by inserting each element in l into an initially empty tree
def treefromlist(l):
    t = emptytree()
    for x in range(0, (len(l))):
        t = insert(t, l[x])
    return t


def inorderwalk(t):  # print all the keys in tree t in sorted order
    if t[0]:  # if the root of the tree is not nil
        if t[1]:  # if there is a left branch
            inorderwalk(t[1])  # walk through the left branch
        print(t[0], end=" ")    # print the root after checking all the nodes to the left (the root is now the smallest)
        if t[2]:  # if there is a right branch
            inorderwalk(t[2])  # walk through the right branch


def delete(t, k):
    # remove k from tree t
    t = to_list(t)  # so its elements can be changed
    parent, key = find_node_and_parent(t, k)
    if not key:
        raise KeyError  # k not found
   
    if None not in (key[1], key[2]):   # k has two children
        small, parent = find_min(key[2], key)  # find the smallest node in the subtree
        key[0] = small[0]
        key = small

    if (not key[1]) and (not key[2]):  # k is a leaf
        # set parent.left or .right to None, no subsequent children to care about
        if not parent:  # you deleted the only item in the tree
            t = None
        elif key[0] < parent[0]:
            parent[1] = None
        else:
            parent[2] = None

    elif (not key[1]) or (not key[2]):  # k has one child
        # c is the child of k which isn't None
        c = key[1]  # guess that its the left child
        if not c: 
            c = key[2]
        if not parent:  # you are deleting the root of the tree
            t = c
        elif key[0] < parent[0]:
            parent[1] = c
        else:
            parent[2] = c
    t = to_tuple(t)
    return t


def find_node_and_parent(tree, x):
    # locate a node with key x in the tree, return that node and its parent
    parent = None  
    current = tree
    while current and (current[0] != x):
        parent = current
        if x < current[0]:
            current = current[1]
        else:
            current = current[2]
    return parent, current


def find_min(node, parent):
    #  Return the smallest element under node and its parent.
    if node is None: 
        return None
    while node[1] is not None:
        parent = node
        node = node[1]
    return node, parent
        

def to_list(t):
    return list(map(to_list, t)) if isinstance(t, (list, tuple)) else t


def to_tuple(t):
    return tuple(map(to_tuple, t)) if isinstance(t, (tuple, list)) else t


# TODO delete this before submission, just here for testing
if __name__ == "__main__":
    tree = treefromlist([4, 2, 6, 5, 8, 9])
    print(tree)
    inorderwalk(tree)
    tree = insert(tree, 7)
    tree = delete(tree, 7)
    tree = insert(tree, 10)
    tree = insert(tree, 1)
    print(tree)
    tree = delete(tree, 4)
    print(tree)
    tree2 = treefromlist([3])
    tree2 = delete(tree2, 3)
    print(tree2)
