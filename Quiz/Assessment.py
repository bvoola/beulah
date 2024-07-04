import os
import random
import re
import time
import Logger
import Util


def assess(QUESTIONS,noOfQuestions):
    correct_answers = 0
    incorrect_answers = 0
    wrong_answers = ''
    start_time = time.time()
    questionAns =1

    for i in range(noOfQuestions):

        random_element = random.choice(QUESTIONS)
        random_element_str = str(random_element)
        question, correct_answer = random_element_str.split(",")

        pattern = r"'(.*?)'"
        matches = re.findall(pattern, question)
        matchesAns = re.findall(pattern, correct_answer)

        Util.clear()
        print(questionAns)
        print(".")
        answer = input(f"{matches[0]}= ")
        if answer == matchesAns[0]:
            print("Correct!")
            time.sleep(.5)
            Util.clear()
            correct_answers = correct_answers + 1
        else:
            print(f"The answer is {matchesAns[0]!r}, not {answer!r}")
            time.sleep(1)
            Util.clear()
            incorrect_answers = incorrect_answers + 1
            wrong_answers = wrong_answers + matches[0] + "=" + answer + "\n"
        questionAns = questionAns + 1

    percentage = int(round((correct_answers / (correct_answers + incorrect_answers)) * 100, 0))
    print(f"You have answered {correct_answers} out of {correct_answers + incorrect_answers} - "
          f"So you got {percentage} %")

    Logger.logIt(f"You have answered {correct_answers} out of {correct_answers + incorrect_answers} - "
          f"So you got {percentage} %")
    if percentage < 70:
        Logger.logIt(f"Oh NO !")
    if 70 < percentage < 75:
        Logger.logIt(f" Hmm... !")
    if 75 < percentage < 85:
        Logger.logIt(f"Okay ! All the best - Good try !")
    if 80 < percentage < 85:
        Logger.logIt(f"Good Job !")
    if 85 < percentage < 90:
        Logger.logIt(f"Very Good Job !")
    if 90 < percentage < 100:
        Logger.logIt(f"Excellent !")
    if percentage >= 100:
        Logger.logIt(f"Awesome !")
    print('Wrong Answers List :')
    print(wrong_answers)
    Logger.logIt("Wrong Answers List\n" +wrong_answers)
    end_time = time.time()
    timeTaken = round(end_time - start_time)
    print("Time taken is " + str(timeTaken) + "seconds")
    Logger.logIt("Time taken is " + str(timeTaken) + "seconds")
    print("Average time taken to answer" + str(timeTaken / (questionAns-1)) + "seconds")
    Logger.logIt("Average time taken to answer" + str(timeTaken / (questionAns-1) )+ "seconds")
    Logger.logIt("------End------")