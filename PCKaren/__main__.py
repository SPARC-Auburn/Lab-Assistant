from properties import *
from DefaultSuite import *

karen = Assistant("Karen", "English", "To assist SPARC members", "SPARC Lab")

#Passes information from Assistant to the found suite.files
def sendCommands(cmd):
	
	if DefaultSuiteMethod(karen, karen.intent, cmd) == False:
		pass
	else:
		print "No command recognized"
			
			
	#Searches for files with "#suite.file" to import as a suite
def searchSuites():
	with open("SuiteList.txt", "w") as suiteList:
		for file in os.listdir(os.curdir):
			if file.endswith(".py"):
				f = open(file, "r")
				firstLine = f.readline()
				if firstLine.__contains__("#suite.file"):
					print "Imported " + file[:-3]
					global newSuite
					newSuite = __import__(file[:-3], globals(), locals())
					suiteList.write(file[:-3])
	suiteList.close()	
		
while True:

	karen.Listen("")
	sendCommands(karen.userCommand)