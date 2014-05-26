from FSelement import Element

class File(Element):
  
  def __new__(self, name, parent, size):
    super().__new__(self, name, parent)
    if isinstance(size, int):
      self.__size = size
    else:
      raise Exception()
  
  def getSize():
    return __size
  
  def getInfo():
    return ""
