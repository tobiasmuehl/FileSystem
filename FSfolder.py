from FSelement import Element

root = 0;
def getRoot():
  return root

def setRoot(r):
  root = r

class Folder(Element):
  
  
  
  def __new__(self, name, parent=None):
    if getRoot == 0:
      setRoot(self)
    elif parent == "" and isinstance(getRoot(), Folder):
      raise Exception("Root Folder already exists")

    Folder.__init__(self, name, parent)
    
  def __init__(self, name, parent=getRoot()):
    super().__new__(self, name, parent)
    self.__contains = [];
    self.__changeDate = None;


  def getSize(self):
    self.__size = 0
    for element in self.__contains:
      self.__size += element.getSize()
    return self.__size

  def addFile(self, file):
    self.__contains.push(file)

  def drawTree():
    drawTree(root)

  def drawTree(self):
    for x in obj.__contains:
      if isinstance(x, Folder):
        print(x.getName())
        drawTree(x)
  
  def getChangeDate(self):
    for x in obj.__contains:
      if isinstance(x, Folder):
        x.getChangeDate()
        
      if isinstance(x, File):
        new = x.getChangeDate();
      
      if new > changeDate:
        changeDate = new
    
    return new

  def setRoot(root):
    root = root
    
