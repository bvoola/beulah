
# quiz.py
import time
from datetime import datetime
from os import system

QUESTIONS = [
  

 
("11-1","10"),
("9-1","8"),
("4-2","2"),
("12-5","7"),
("7-5","2"),
("12-4","8"),
("8-6","2"),
("6-1","5"),
("11-10","1"),
("5-3","2"),
("9-7","2"),
("8-7","1"),
("10-6","4"),
("12-3","9"),
("5-1","4"),
("9-6","3"),
("12-6","6"),
("7-2","5"),
("11-2","9"),
("6-2","4"),
("10-8","2"),
("10-5","5"),
("12-2","10"),
("8-4","4"),
("12-8","4"),
("11-6","5"),
("3-2","1"),
("7-1","6"),
("10-3","7"),
("9-5","4"),
("11-5","6"),
("8-1","7"),
("12-7","5"),
("9-3","6"),
("6-5","1"),
("4-1","3"),
("11-8","3"),
("7-6","1"),
("8-2","6"),
("10-1","9"),
("2-1","1"),
("11-7","4"),
("12-10","2"),
("5-4","1"),
("10-4","6"),
("9-2","7"),
("6-4","2"),
("11-9","2"),
("8-3","5"),
("12-9","3"),
("11-4","7"),
("3-1","2"),
("5-2","3"),
("10-9","1"),
("7-3","4"),
("12-11","1"),
("6-3","3"),
("9-8","1"),
("11-3","8"),
("4-3","1"),
("12-1","11"),
("7-4","3"),
("8-5","3"),
("11-11","0"),
("9-4","5"),
("10-7","3"),
("10-10","0"),
("11-12","-1"),
("7-7","0"),
("12-12","0"),
("6-6","0"),
("8-8","0"),
("5-5","0"),
("9-9","0"),
("4-4","0"),
("3-3","0"),
("2-2","0"),
("1-1","0"),
("11-1","10"),
("9-1","8"),
("4-2","2"),
("12-5","7"),
("7-5","2"),
("12-4","8"),
("8-6","2"),
("6-1","5"),
("11-10","1"),
("5-3","2"),
("9-7","2"),
("8-7","1"),
("10-6","4"),
("12-3","9"),
("5-1","4"),
("9-6","3"),
("12-6","6"),
("7-2","5"),
("11-2","9"),
("6-2","4"),
("10-8","2"),
("10-5","5"),
("12-2","10"),
("8-4","4"),
("12-8","4"),
("11-6","5"),
("3-2","1"),
("7-1","6"),
("10-3","7"),
("9-5","4"),
("11-5","6"),
("8-1","7"),
("12-7","5"),
("9-3","6"),
("6-5","1"),
("4-1","3"),
("11-8","3"),
("7-6","1"),
("8-2","6"),
("10-1","9"),
("2-1","1"),
("11-7","4"),
("12-10","2"),
("5-4","1"),
("10-4","6"),
("9-2","7"),
("6-4","2"),
("11-9","2"),
("8-3","5"),
("12-9","3"),
("11-4","7"),
("3-1","2"),
("5-2","3"),
("10-9","1"),
("7-3","4"),
("12-11","1"),
("6-3","3"),
("9-8","1"),
("11-3","8"),
("4-3","1"),
("12-1","11"),
("7-4","3"),
("8-5","3"),
("11-11","0"),
("9-4","5"),
("10-7","3"),
("10-10","0"),
("11-12","-1"),
("7-7","0"),
("12-12","0"),
("6-6","0"),
("8-8","0"),
("5-5","0"),
("9-9",""),
("4-4","0"),
("3-3","0"),
("2-2","0"),
("1-1","0"),
("11-1","10"),
("9-1","8"),
("4-2","2"),
("12-5","7"),
("7-5","2"),
("12-4","8"),
("8-6","2"),
("6-1","5"),
("11-10","1"),
("5-3","2"),
("9-7","2"),
("8-7","1"),
("10-6","4"),
("12-3","9"),
("5-1","4"),
("9-6","3"),
("12-6","6"),
("7-2","5"),
("11-2","9"),
("6-2","4"),
("10-8","2"),
("10-5","5"),
("12-2","10"),
("8-4","4"),
("12-8","4"),
("11-6","5"),
("3-2","1"),
("7-1","6"),
("10-3","7"),
("9-5","4"),
("11-5","6"),
("8-1","7"),
("12-7","5"),
("9-3","6"),
("6-5","1"),
("4-1","3"),
("11-8","3"),
("7-6","1"),
("8-2","6"),
("10-1","9"),
("2-1","1"),
("11-7","4"),
("12-10","2"),
("5-4","1"),
("10-4","6"),
("9-2","7"),
("6-4","2"),
("11-9","2"),
("8-3","5"),
("12-9","3"),
("11-4","7"),
("3-1","2"),
("5-2","3"),
("10-9","1"),
("7-3","4"),
("12-11","1"),
("6-3","3"),
("9-8","1"),
("11-3","8"),
("4-3","1"),
("12-1","11"),
("7-4","3"),
("8-5","3"),
("11-11","0"),
("9-4","5"),
("10-7","3"),
("10-10","0"),
("11-12","-1"),
("7-7","0"),
("12-12","0"),
("6-6","0"),
("8-8","0"),
("5-5","0"),
("9-9","0"),
("4-4","0"),
("3-3","0"),
("2-2","0"),
("1-1","0"),
("11-1","10"),
("9-1","8"),
("4-2","2"),
("12-5","7"),
("7-5","2"),
("12-4","8")





]

correct_answers = 0
incorrect_answers = 0
wrong_answers = ''
start_time = time.time()
noofquestions = 0

# print the current timestamp

for question, correct_answer in QUESTIONS:
   noofquestions = noofquestions + 1

   system("cls")
   print(noofquestions)
   print(".")
   answer = input(f"{question}= ")

   if answer == correct_answer:
       print("Correct!")
       time.sleep(.5)
       system("cls")
       correct_answers = correct_answers + 1
   else:
       print(f"The answer is {correct_answer!r}, not {answer!r}")
       time.sleep(1)
       system("cls")
       incorrect_answers = incorrect_answers + 1
       wrong_answers = wrong_answers + question + "=" + answer + "\r\n"


percentage = int(round((correct_answers / (correct_answers + incorrect_answers)) * 100, 0))
print(f"You have answered {correct_answers} out of {correct_answers + incorrect_answers} - "
     f"So you got {percentage} %")

if percentage < 70:
   print(f"Oh NO !")
if 70 < percentage < 75:
   print(f" Hmm... !")
if 75 < percentage < 85:
   print(f"Okay ! All the best - Good try !")
if 80 < percentage < 85:
   print(f"Good Job !")
if 85 < percentage < 90:
   print(f"Very Good Job !")
if 90 < percentage < 100:
   print(f"Excellent !")
if percentage >= 100:
   print(f"Awesome !")

print('Wrong Answers List :')
print(wrong_answers)


end_time = time.time()
timeTaken = round(end_time - start_time)
print("Time taken is "+str(timeTaken)+"seconds")
print("Average time taken to answer" + str(timeTaken/int(noofquestions))+"seconds")





