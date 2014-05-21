class Folder(Element):
  def __init__(self, name, size):
    super().__init__(name, size)
    self.__contains = [];

  def getSize(self):
    self.__size = 0
    for element in self.__contains:
      self.__size += element.getSize()
    return self.__size
    
  
    
