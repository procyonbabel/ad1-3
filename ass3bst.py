# For compatability between Python versions 2.x and 3.x

# For all versions, print function should be in the same form: e.g. print(0)

from __future__ import print_function





# Name 1:

# Name 2:

# Name 3:



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
