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

  def getType(self):
    return "Not a File or Folder"
  
  def printInfo(self):
    print (self.getName().ljust(20), str(self.getSize()).ljust(20), self.getType().ljust(14), str(self.getChangeDate()).ljust(26), sep="")
  
  def setName(self, name):
    if isinstance( name, str ):
      self.__name = name
      return true
    else:
      raise Exception()

class Folder(Element):

    root = None
    
    def __init__(self, name, parent):
      if parent == None:
          if Folder.root == None:
            Folder.root = self
            parent = self
          else: raise Exception()

      self.__content = [];
      
      Element.__init__(self, name, parent)
    
    # Baumansicht zeichnen:
    def drawTree():
        print('Baumansicht'.center(80));
        print(''.ljust(80, '='))
        Folder.root.drawFolders(0)

    # Rekursive Fkt zum Zeichnen eines Ordners mit allen seinen Unterordnern (Für Baumansicht):
    def drawFolders(self, level):
        space = "+"
        for i in range(0, level):
          space = "--" + space
      
        print(space, self.getName())
    
        for x in self.__content:
          if isinstance(x, Folder):
            x.drawFolders(level+1)

    def getSize(self):
        self.__size = 0
        for element in self.__contains:
          self.__size += element.getSize()
        return self.__size

    def addElement(self, e):
        self.__content.append(e)
  
    def getChangeDate(self):
        last = self.__changeDate
        for x in self.__content:
          changeDate = x.getChangeDate();
          if changeDate > last:
            last = changeDate
        return last

    def listView(self):
      print('Detailansicht'.center(80));
      print(''.ljust(80, '='))

      print("Dateiname".ljust(20), "Größe".ljust(20), "Typ".ljust(14), "Änderungsdatum".ljust(26), sep="")
      print("".ljust(80, '='))
      for x in self.__content:
        x.printInfo()

    def getType(self):
      return "Folder"

class File(Element):
  
  def __init__(self, name, parent, size):
    Element.__init__(self, name, parent)
    if isinstance(size, int):
      self.__size = size
    else:
      raise Exception()
  
  def getSize(self):
    return self.__size

  def getType(self):
    extensions = {
    'txt': 'Text File',
    'mvkv': 'Matroska Video File'
    }
    try:
      t = extensions[self.getName().split('.')[-1]]
    except(Exception):
      t = "Unknown"
    
    return t
