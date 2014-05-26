from FSfolder import Folder

class RootFolder(Folder):
	def __new__(self, name):
		super().setRoot(self)
		super().__init__(self, name, self)