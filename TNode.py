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
        #inorder prit
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
        
        
if __name__ == "__main__":
    root = Node(10)
    root.insert(20)
    root.insert(21)
    root.insert(3)
    root.insert(1)
    root.insert(4)
    root.insert(6)
    root.insert(22)
    root.insert(50)
    root.printT()

    print("Height is %d" % root.calHeight())
        

