"""
Program Name: __main__.py
Organization: Student Projects and Research Committee at Auburn University
Project: Lab Assistant
Description: The main file of the lab assistant python project.  Searches directory for suites and passes information
from assistant to the found suite files.
"""
from properties import *
from defaultsuite import *
from labsuite import *
from homesuite import *

karen = Assistant("Karen", "English", "to assist SPARC members", "SPARC Lab")


# TODO: Figure out more elegant solution to importing suites
def searchsuites():
    """Searches for files with "#suites.file" to import as a suites"""
    with open("SuiteList.txt", "w") as suiteList:
        for pyfile in os.listdir(os.curdir):
            if pyfile.endswith(".py"):
                f = open(pyfile, "r")
                firstline = f.readline()
                if firstline.__contains__("#suites.file"):
                    print ("Imported " + pyfile[:-3])
                    global newsuite
                    newsuite = __import__(pyfile[:-3], globals(), locals())
                    suiteList.write(pyfile[:-3])
    suiteList.close()


def main():
    """Main function that keeps Karen listening and responding"""
    defaultsuite = DefaultSuite()
    labsuite = LabSuite()
    while True:
        karen.listen("")
        user_message = str(karen.userCommand)
        if len(user_message) > 0:
            whattosay = None
            if defaultsuite.checkcommand(user_message) is not None:
               whattosay = defaultsuite.response
            elif labsuite.checkcommand(user_message) is not None:
                whattosay = labsuite.response
            # elif homesuitemethod(karen, karen.intent, user_message):
            #     pass
            else:
                whattosay = "I did not understand what you said"
            karen.speak(whattosay)

if __name__ == "__main__":
    main()
