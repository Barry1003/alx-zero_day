#getting the number of tree
tree_height = input("how tall is thge tree : ")
tree_height = int(tree_height)
#getting the starting space for the top of the tree
spaces = tree_height - 1

#there is one hash to start  that will be incremented
hash = 1
##save stump sapcestill latrer
stump_sapces = tree_height - 1

while tree_height != 0:
    for i in range(spaces):
        print(' ', end="")

    for i in range(hash):
        print ('#', end="")
    print()

    spaces -= 1
    hash += 2
    tree_height -=1

for i in range(stump_sapces):
    print(' ', end="")

print("#")