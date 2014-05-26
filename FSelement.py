import datetime

class Element(object):
  
  def __new__(self, name, parent):
    # if isinstance( name, str ) and isinstance( parent, Folder ):
      self.__name = name
      self.__changeDate = datetime.datetime.now()
      self.__parent = parent
    # else:
    #   raise Exception()

  def getName(self):
    return self.__name
    
  def getSize(self):
    return 0
  
  def getChangeDate(self):
    return self.__changeDate
  
  def getInfo(self):
    return
  
  def setName(self, name):
    if isinstance( name, str ):
      self.__name = name
      return true
    else:
      raise Exception()
