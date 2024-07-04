import os
import sys
import Logger
import Assessment
import Util

Util.clear()
print('Welcome to Multiplication Table 12')
Logger.logIt(os.path.splitext(os.path.basename(__file__))[0])
noOfQuestions = int(sys.argv[1])

QUESTIONS = [
("1 * 12", "12")  ,
("2 * 12", "24")  ,
("3 * 12", "36")  ,
("4 * 12", "48")  ,
("5 * 12", "60")  ,
("6 * 12", "72")  ,
("7 * 12", "84")  ,
("8 * 12", "96")  ,
("9 * 12", "108")  ,
("10 * 12", "120")  

]

Assessment.assess(QUESTIONS, noOfQuestions)
