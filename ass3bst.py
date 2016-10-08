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

#TODO: Does anyone know how to print all the numbers in a line?
# used print(t[0], end= " ") but it doesn't look nice...
def inorderwalk(t): # print all the keys in tree t in sorted order
    if t[0] != None: # if the root of the tree is not nil
        if t[1] !=None: # if there is a left branch
            inorderwalk(t[1]) # walk through the left branch 
        print(t[0])    # print the root after checking all the nodes to the left (the root is now the smallest)
        if t[2] !=None: # if there is a right branch
            inorderwalk(t[2]) # walk through the right branch

    
