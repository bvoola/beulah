import os
import sys
import Logger
import Assessment
import Util

Util.clear()
print('Welcome to Multiplication Table 13')
Logger.logIt(os.path.splitext(os.path.basename(__file__))[0])
noOfQuestions = int(sys.argv[1])

QUESTIONS = [

("1 * 13", "13")  ,
("2 * 13", "26")  ,
("3 * 13", "39")  ,
("4 * 13", "52")  ,
("5 * 13", "65")  ,
("6 * 13", "78")  ,
("7 * 13", "91")  ,
("8 * 13", "104")  ,
("9 * 13", "117")  ,
("10 * 13", "130")  

]

Assessment.assess(QUESTIONS, noOfQuestions)
