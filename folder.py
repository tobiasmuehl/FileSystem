class Folder(Element):
  __root = None;
  __changeDate = None;
  
  def __init__(self, name, size, parent):
    super().__init__(name, size, parent)
    self.__contains = [];
    
    if parent == None and __root == None:
      __root = self
    elif parent == None and isinstance(__root, Folder):
      raise Exception("Root Folder already exists")

  def getSize(self):
    self.__size = 0
    for element in self.__contains:
      self.__size += element.getSize()
    return self.__size

  def addFile(self, file):
    self.__contains.push(file)

  def drawTree():
    drawTree(__root)

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
    
