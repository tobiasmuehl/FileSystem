from FSelement import Element
import datetime

class Folder(Element):

  root = None
  
  def __init__(self, name, parent):
    self.__changeDate = datetime.datetime.now()
    Element.__init__(self, name, parent)
    self.__content = [];
    if parent == None:
      if Folder.root == None:
        Folder.root = self
        parent = self
      else: raise Exception()
    else:
      if Folder.root == None:
        raise Exception()
      else: 
        self.__parent = parent
        parent.addElement(self)
    

  
  def drawTree():
    print('Baumansicht'.center(80));
    print(''.ljust(80, '='))
    Folder.root.drawFolders(0)

  def drawFolders(self, level):
    space = ""
    for i in range(0, level):
      space += "+"
  
    print(space, self.getName())

    for x in self.__content:
      if isinstance(x, Folder):
        x.drawFolders(level+1)

  def getSize(self):
      self.__size = 0
      for element in self.__content:
        self.__size += element.getSize()
      return self.__size

  def addElement(self, e):
      self.__content.append(e)
      e.__parent = self

  def getChangeDate(self):
      last = self.__changeDate
      for x in self.__content:
        changeDate = x.getChangeDate();
        if changeDate > last:
          last = changeDate
      return last

  # def printInfo(self):
  #   print (self.getName().ljust(20), str(self.getSize()).ljust(20), self.getType().ljust(14), str(self.getChangeDate()).ljust(26), sep="")

  def listView(self):
    print('Detailansicht'.center(80));
    print(''.ljust(80, '='))

    print("Dateiname".ljust(20), "Größe".ljust(20), "Typ".ljust(14), "Änderungsdatum".ljust(26), sep="")
    print("".ljust(80, '='))
    for x in self.__content:
      x.printInfo()
      

  def getType(self):
    return "Folder"
