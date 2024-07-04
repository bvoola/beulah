import os
import sys
import Logger
import Assessment
import Util

Util.clear()
print('Welcome to Subtraction below 12')
Logger.logIt('Subtraction below 12')
Logger.logIt(os.path.splitext(os.path.basename(__file__))[0])
noOfQuestions = int(sys.argv[1])

QUESTIONS = [
    ("1-0", "1"),
    ("2-0", "2"),
    ("2-1", "1"),
    ("3-0", "3"),
    ("3-1", "2"),
    ("3-2", "1"),
    ("4-0", "4"),
    ("4-1", "3"),
    ("4-2", "2"),
    ("4-3", "1"),
    ("5-0", "5"),
    ("5-1", "4"),
    ("5-2", "3"),
    ("5-3", "2"),
    ("5-4", "1"),
    ("6-0", "6"),
    ("6-1", "5"),
    ("6-2", "4"),
    ("6-3", "3"),
    ("6-4", "2"),
    ("6-5", "1"),
    ("7-0", "7"),
    ("7-1", "6"),
    ("7-2", "5"),
    ("7-3", "4"),
    ("7-4", "3"),
    ("7-5", "2"),
    ("7-6", "1"),
    ("8-0", "8"),
    ("8-1", "7"),
    ("8-2", "6"),
    ("8-3", "5"),
    ("8-4", "4"),
    ("8-5", "3"),
    ("8-6", "2"),
    ("8-7", "1"),
    ("9-0", "9"),
    ("9-1", "8"),
    ("9-2", "7"),
    ("9-3", "6"),
    ("9-4", "5"),
    ("9-5", "4"),
    ("9-6", "3"),
    ("9-7", "2"),
    ("9-8", "1"),
    ("10-0", "10"),
    ("10-1", "9"),
    ("10-2", "8"),
    ("10-3", "7"),
    ("10-4", "6"),
    ("10-5", "5"),
    ("10-6", "4"),
    ("10-7", "3"),
    ("10-8", "2"),
    ("10-9", "1"),
    ("11-0", "11"),
    ("11-1", "10"),
    ("11-2", "9"),
    ("11-3", "8"),
    ("11-4", "7"),
    ("11-5", "6"),
    ("11-6", "5"),
    ("11-7", "4"),
    ("11-8", "3"),
    ("11-9", "2"),
    ("11-10", "1"),
    ("12-0", "12"),
    ("12-1", "11"),
    ("12-2", "10"),
    ("12-3", "9"),
    ("12-4", "8"),
    ("12-5", "7"),
    ("12-6", "6"),
    ("12-7", "5"),
    ("12-8", "4"),
    ("12-9", "3"),
    ("12-10", "2"),
    ("12-11", "1"),
    ("13-0", "13"),
    ("13-1", "12"),
    ("13-2", "11"),
    ("13-3", "10"),
    ("13-4", "9"),
    ("13-5", "8"),
    ("13-6", "7"),
    ("13-7", "6"),
    ("13-8", "5"),
    ("13-9", "4"),
    ("13-10", "3"),
    ("13-11", "2"),
    ("13-12", "1"),
    ("14-0", "14"),
    ("14-1", "13"),
    ("14-2", "12"),
    ("14-3", "11"),
    ("14-4", "10"),
    ("14-5", "9"),
    ("14-6", "8"),
    ("14-7", "7"),
    ("14-8", "6"),
    ("14-9", "5"),
    ("14-10", "4"),
    ("14-11", "3"),
    ("14-12", "2"),
    ("14-13", "1"),
    ("15-0", "15"),
    ("15-1", "14"),
    ("15-2", "13"),
    ("15-3", "12"),
    ("15-4", "11"),
    ("15-5", "10"),
    ("15-6", "9"),
    ("15-7", "8"),
    ("15-8", "7"),
    ("15-9", "6"),
    ("15-10", "5"),
    ("15-11", "4"),
    ("15-12", "3"),
    ("15-13", "2"),
    ("15-14", "1")]

Assessment.assess(QUESTIONS, noOfQuestions)