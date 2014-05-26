from FSelement import Element


class Folder(Element):
  def __init__(self, name, parent):
    super.__init__(self, name, parent)
    self.__content = [];


  def getSize(self):
    self.__size = 0
    for element in self.__contains:
      self.__size += element.getSize()
    return self.__size

  def addFile(self, file):
    self.__content.push(file)

  def drawTree(self, level):
    print(self.getName())
    for x in self.__content:
      if isinstance(x, Folder):
        x.drawTree(level+1)
  
  def getChangeDate(self):
    last = self.__changeDate
    for x in self.__content:
      changeDate = x.getChangeDate();
      if changeDate > last:
        last = changeDate
    return last

  def setRoot(root):
    root = root
    
