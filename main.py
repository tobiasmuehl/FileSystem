import datetime
from FSelement import Element
from FSfolder import Folder
from FSRootFolder import RootFolder
from FSfile import File

def drawTree(root):
  Folder.drawTree(root)

root = RootFolder("/")
fo = Folder("folder", root)
fo2 = Folder("folder", fo)
f = File("Filename", root, 10)
