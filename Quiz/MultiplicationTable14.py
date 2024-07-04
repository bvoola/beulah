import os
import sys
import Logger
import Assessment
import Util

Util.clear()
print('Welcome to Multiplication Table 14')
Logger.logIt(os.path.splitext(os.path.basename(__file__))[0])
noOfQuestions = int(sys.argv[1])

QUESTIONS = [


("1 * 14", "14"),
("2 * 14", "28"),
("3 * 14", "42"),
("4 * 14", "56"),
("5 * 14", "70"),
("6 * 14", "84"),
("7 * 14", "98"),
("8 * 14", "112"),
("9 * 14", "126"),
("10 * 14", "140")

]

Assessment.assess(QUESTIONS, noOfQuestions)
