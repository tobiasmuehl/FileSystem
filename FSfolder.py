from FSelement import Element


class Folder(Element):
  def __init__(self, name, parent):
    Element.__init__(self, name, parent)
    self.__contains = [];
    self.__changeDate = None;


  def getSize(self):
    self.__size = 0
    for element in self.__contains:
      self.__size += element.getSize()
    return self.__size

  def addFile(self, file):
    self.__contains.push(file)

  def drawTree(self):
    for x in self.__contains:
      if isinstance(x, Folder):
        print(x.getName())
        drawTree(x)
  
  def getChangeDate(self):
    for x in self.__contains:
      if isinstance(x, Folder):
        x.getChangeDate()
        
      if isinstance(x, File):
        new = x.getChangeDate();
      
      if new > changeDate:
        changeDate = new
    
    return new

  def setRoot(root):
    root = root
    