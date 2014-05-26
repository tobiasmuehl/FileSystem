from FSfolder import Folder

class RootFolder(Folder):
	def __new__(self, name):
		self.__contains = [];
		self.__changeDate = None;

root = RootFolder("/")