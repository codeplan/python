import random
import sys
import copy

class Node:
    def __init__(self, value):
        self.leftc = None
        self.rightc = None
        self.value = value
    

    def insert(self, data):
        if(self == None):
            self.value = Node(data)
        elif(self.value > data):
                if(self.leftc == None):
                    self.leftc = Node(data)
                else:
                    self.leftc.insert(data)
        else:
            if(self.rightc == None):
                self.rightc = Node(data)
            else:
                self.rightc.insert(data)
            


    def printT(self):
        #inorder print
        if(self == None):
            return
        else:
            if(self.leftc != None):
                self.leftc.printT()
            print("->"+str(self.value))
            if(self.rightc != None):
                self.rightc.printT()
        
    def calHeight(self):
        if (self == None):
            return 0
        else:
            l_height = 0
            r_height = 0
            if(self.leftc != None):
                l_height = self.leftc.calHeight()
            if(self.rightc != None):
                r_height = self.rightc.calHeight()
            return 1 + max(l_height, r_height)

    def is_tree_identical(self, tree):
        if ((self == None) and (tree == None)):
            print('both trees are None')
            return

        if(((self.leftc != None) and (tree.leftc == None)) or ((self.leftc == None) and (tree.leftc != None)) ):
            print("Left Tree is not identical of !!"+ str(self.value)+" and "+ str(tree.value))
            sys.exit()
        elif ((self.leftc != None) and (tree.leftc != None)):
            self.leftc.is_tree_identical(tree.leftc)
        if self.value != tree.value:
            print("Trees are not identical!!")
            sys.exit()


        if(((self.rightc != None) and (tree.rightc == None)) or ((self.rightc == None) and (tree.rightc != None)) ):
            print("Right Tree is not identical of !!"+ str(self.value)+" and "+ str(tree.value))
            sys.exit()
        elif ((self.rightc != None) and (tree.rightc != None)):
            self.rightc.is_tree_identical(tree.rightc)


    def is_tree_mirror(self, tree):
        
        
        
class util:
    def get_random_list(min, max, size):
        local_list = []

        while(size):
            local_list.append(random.randrange(min, max))
            size -= 1
        return local_list
        
if __name__ == "__main__":
    root1 = Node(10)
    lst1 = util.get_random_list(0,100,10)
    print(lst1)
    for x in lst1:
        root1.insert(x)
    root1.printT()

    root2 = Node(10)
    lst2 = util.get_random_list(0,100,10)
    print(lst2)
    for x in lst2:
        root2.insert(x)
    #root2.printT()

    print('----')
    root3 = copy.copy(root1)
    root2.printT()
    
    root1.is_tree_identical(root2)
    #print("Height is %d" % root.calHeight())
        

