import datetime

class Element(object):
  
  def __init__(self, name, parent):
    if isinstance( name, str ) and isinstance( parent, Folder ):
      self.__name = name
      self.__changeDate = datetime.datetime.now()
      self.__parent = parent
      if self != Folder.root: parent.addElement(self)
    else:
      raise Exception()

  def getName(self):
    return self.__name
    
  def getSize(self):
    return 0
  
  def getChangeDate(self):
    return self.__changeDate


  def printInfo(self):
    print (self.getName().ljust(20), str(self.getSize()).ljust(20), self.getType().ljust(14), str(self.getChangeDate()).ljust(26), sep="")

  def getType(self):
    return "Not a File or Folder"
  
  def setName(self, name):
    if isinstance( name, str ):
      self.__name = name
      return true
    else:
      raise Exception()
