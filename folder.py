class Folder(Element):
  root = None;
  
  def __init__(self, name, size, parent):
    super().__init__(name, size, parent)
    self.__contains = [];
    
    if parent == None and root == None:
      root = self
    elif parent == None and isinstance(root, Folder):
      raise Exception("Root Folder already exists")

  def getSize(self):
    self.__size = 0
    for element in self.__contains:
      self.__size += element.getSize()
    return self.__size
    
  def addFile(self, file):
    self.__contains.push(file)
    
  def drawTree(self):
    x = True
    var root;
    while (x):
      root = 
      
  
  def drawTree(self):
    Folder.drawTree();
    
