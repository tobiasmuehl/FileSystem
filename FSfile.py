from FSelement import Element

class File(Element):
  
  def __init__(self, name, parent, size):
    Element.__init__(self, name, parent)
    if isinstance(size, int):
      self.__size = size
    else:
      raise Exception()
  
  def getSize(self):
    return self.__size
  
  def getInfo(self):
    return ""
