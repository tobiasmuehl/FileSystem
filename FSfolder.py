from FSelement import Element


class Folder(Element):

    root = None
    
    def __init__(self, name, parent):
        Element.__init__(self, name, parent)
        if parent == None:
            if Folder.root == None:
                Folder.root = self
                parent = self
            else: raise Exception()
        else:
            if Folder.root == None:
                raise Exception()
            else: self.__parent = parent
        self.__content = [];
    
    def drawTree():
        Folder.root.drawFolders(0)

    def drawFolders(self, level):
        space = ""
        for i in range(0, level):
            space += "+"
      
        print(space, self.getName())
    
        for x in self.__content:
            if isinstance(x, Folder):
                x.drawFolders(level+1)

    def getSize(self):
        self.__size = 0
        for element in self.__contains:
            self.__size += element.getSize()
        return self.__size

    def addElement(self, e):
        self.__content.append(e)
  
    def getChangeDate(self):
        last = self.__changeDate
        for x in self.__content:
            changeDate = x.getChangeDate();
            if changeDate > last:
                last = changeDate
        return last

    def setRoot(root):
        root = root
    
