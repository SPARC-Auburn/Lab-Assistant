"""
Program Name: manage_suites.py
Organization: Student Projects and Research Committee at Auburn University
Project: Lab Assistant
Description: Collects all of the suites and parses through each to determine correct response.
"""

from suites.defaultsuite import *
from suites.labsuite import *
from suites.homesuite import *
from suites.weathersuite import *
from suites.fallbacksuite import *

suites = [DefaultSuite(), LabSuite(), HomeSuite(), WeatherSuite(), FallBackSuite()]


def getresponse(user_message):
    if len(user_message) > 0:
        for suite in suites:
            if suite.checkcommand(user_message) is not None:
                return suite.response


# def searchsuites():
#     """Searches for files with "#suites.file" to import as a suites"""
#     with open("SuiteList.txt", "w") as suiteList:
#         for pyfile in os.listdir(os.curdir):
#             if pyfile.endswith(".py"):
#                 f = open(pyfile, "r")
#                 firstline = f.readline()
#                 if firstline.__contains__("#suites.file"):
#                     print ("Imported " + pyfile[:-3])
#                     global newsuite
#                     newsuite = __import__(pyfile[:-3], globals(), locals())
#                     suiteList.write(pyfile[:-3])
#     suiteList.close()
