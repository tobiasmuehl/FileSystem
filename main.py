import datetime
from FSelement import Element
from FSfolder import Folder
from FSRootFolder import RootFolder
from FSfile import File


fo = Folder("folder", None)
fo2 = Folder("subfolder", fo)
fo.addElement(fo2)
f = File("Filename.txt", fo2, 10)
fo2.addElement(f) # das kann man eig noch in die init von element einbauen fällt mir grad ein
Folder.drawTree()
