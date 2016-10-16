# For compatability between Python versions 2.x and 3.x
# For all versions, print function should be in the same form: e.g. print(0)
from __future__ import print_function
# Name 1: Caroline Appleby
# Name 2: Chiao-ting Fang
# Name 3: Linjing Fu

# Create empty tree
def emptytree ():
    return None

# Insert x into tree t
def insert(t, x):
    if t == None:
        return (x, None , None)
    else:
        key, left, right = t
        if x == key:
            return (key, left, right)
        elif x < key:
            return (key, insert(left, x), right)
        else:
            return (key, left, insert(right, x))

# Create tree by inserting each element in l into an initially empty tree
def treefromlist(l):
    t=emptytree()
    for x in range(0,(len(l))):
        t = insert(t, l[x])
    return t

def inorderwalk(t): # print all the keys in tree t in sorted order
    if t[0]: # if the root of the tree is not nil
        if t[1]: # if there is a left branch
            inorderwalk(t[1]) # walk through the left branch 
        print(t[0], end=" ")    # print the root after checking all the nodes to the left (the root is now the smallest)
        if t[2]: # if there is a right branch
            inorderwalk(t[2]) # walk through the right branch
    print("\n")


def delete(t, k):
    '''Remove item k from the tree.'''
    t = [list(node) for node in t if type(node) == tuple]
    print(t)
    p, q = find_node_and_parent(t, k)
    if not p: 
        raise KeyError      # k not found
   
    if None not in (left(p), right(p)):   # k has two children
        r, q = find_min(right(p), p)
        keyp = key(p)
        keyp = key(r)
        p = r   
    
    if (not left(p)) and (not right(p)):  # k is a leaf
        if not q: # you deleted the only item in the tree
            tree = None  
        elif key(p) < key(q): 
            leftq = left(q) 
            leftq = None
        else: 
            rightq = right(q) 
            rightq = None

    elif (not left(p)) or (not right(p)):      # k has one child
        # c is the child which isn't None
        c = left(p)
        if not c: 
            c = right(p)
        if not q: # that was the root you deleted
            tree = c
        elif key(p) < key(q): 
            leftq = left(q) 
            leftq = c
        else: 
            rightq = right(q) 
            rightq= c
    print(tree)


def find_node_and_parent(tree, x):
    # locate a node with key x in the tree, return that node and its parent
    parent = None  
    current = tree
    while current and (key(current) != x):
        parent = current
        if x < key(current):
            current = left(current)
        else:
            current = right(current)
    return parent, current
    
def find_min(node, parent):
    #Return the smallest element under node and its parent.
    if node is None: 
        return None
    while left(node) is not None:
        parent = node
        node = left(node)
    return (node, parent)
        
def key(tree):
  return tree[0]

def left(tree):
  return tree[1]

def right(tree):
  return tree[2]

def isleaf(tree):
  return left(tree) == None and right(tree) == None


if __name__ == "__main__":
    tree = treefromlist([4, 2, 6, 5, 8 , 9])
    print(tree)
    tree = insert(tree, 7)
    print(tree)
    inorderwalk(tree)
    delete(tree, 5)