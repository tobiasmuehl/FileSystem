
class File(Element):
  
  def __init__(self, name, parent, size):
    super.__init__(name, parent)
    if isinstance(size, int):
      self.__size = size
    else raise Exception()
  
  def getSize():
    return size
  
  def getInfo():
    return ""
