import datetime
from FSelement import Element
from FSfolder import Folder
#from FSRootFolder import RootFolder
from FSfile import File


fo = Folder("folder", None)
fo2 = Folder("subfolder", fo)

f = File("Filename.txt", fo2, 10)


Folder.drawTree()
file2 = File("Filename2.txt", fo2, 99999)

print("")


fo.listView()
