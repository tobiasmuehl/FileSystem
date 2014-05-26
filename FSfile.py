from FSelement import Element
import string

class File(Element):
  
  def __init__(self, name, parent, size):
    Element.__init__(self, name, parent)
    if isinstance(size, int):
      self.__size = size
    else:
      raise Exception()

    parent.addElement(self)
  
  def getSize(self):
    return self.__size


  def getType(self):
    extensions = {
    'txt': 'Text File',
    'mvkv': 'Matroska Video File'
    }
    return extensions[self.getName().split('.')[-1]]
