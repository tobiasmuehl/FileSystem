from FSelement import Element


class Folder(Element):
  def __init__(self, name, parent):
    super.__init__(self, name, parent)
    if parent == None:
      if root == None:
        root = self
        parent = self
      else: raise Exception()
    else:
      if root == None:
        raise Exception()
      else: self.__parent = parent
    self.__content = [];
    
  def drawTree():
    root.drawFolders(0)

  def drawFolders(self, level):
    space = ""
    for i in range(0, level):
      space += "+"
      
    print(self.getName())
    
    for x in self.__content:
      if isinstance(x, Folder):
        x.drawFolders(level+1)

  def getSize(self):
    self.__size = 0
    for element in self.__contains:
      self.__size += element.getSize()
    return self.__size

  def addFile(self, file):
    self.__content.push(file)
  
  def getChangeDate(self):
    last = self.__changeDate
    for x in self.__content:
      changeDate = x.getChangeDate();
      if changeDate > last:
        last = changeDate
    return last

  def setRoot(root):
    root = root
    
