import subprocess
import Logger
import Util

selectedOption = ''
noOfQuestions = ''
Util.clear()
print('Options Available')
print('1. Addition up to 12')
print('2. Subtraction up to 12')
print('3. Multiplication')
print('4. Subtraction up to 15')
print('5. Subtraction up to 20')
print('6. Multiplication Table 12')
print('7. Multiplication Table 13')
print('8. Multiplication Table 14')
selection = input(f"Select the appropriate number : {selectedOption} ")

noOfQuestions = input(f'No of Questions: {noOfQuestions}')
Logger.logIt('-----Start-----')
if selection == '2' :
    subprocess.call(["python", "SubtractionBelow12.py", noOfQuestions])
if selection == '3' :
    subprocess.call(["python", "MultiplicationBelow10.py", noOfQuestions])
if selection == '4' :
    subprocess.call(["python", "SubtractionBelow15.py", noOfQuestions])
if selection == '5' :
    subprocess.call(["python", "SubtractionBelow20.py", noOfQuestions])
if selection == '6' :
    subprocess.call(["python", "MultiplicationTable12.py", noOfQuestions])
if selection == '7' :
    subprocess.call(["python", "MultiplicationTable13.py", noOfQuestions])
if selection == '8' :
    subprocess.call(["python", "MultiplicationTable14.py", noOfQuestions])