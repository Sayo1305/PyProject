import random
import sys
import PIL
from simpleimage import SimpleImage
import json
import winsound
import time
import numpy as np
import matplotlib.pyplot as plt

"""
____________________________________________________________________________________________________________________________________
                                                      QUIZ PROJECT BY (UNNAT DAS)
____________________________________________________________________________________________________________________________________
      This is a Quiz program where one by one 10 question with 4 Option are given and you have to answer correctly.As it is a 
      basic program I add certain feature to give it more value like it also calculate the time is (sec) for answering the each 
      question and if you wish it also provide you graph of your accuracy in which it show the time per sec per question answered
      and i also add sound effect like the intro-sound on the starting of the program and and after each wrong and correct ans
      sound are played and if you marked in correct it also give you the correct answer.  
""" 

#     This is the main program whre it main_menu() function call
def main():
          main_menu()

def main_menu():
          # It is the main screen start with intro sound 
          print("===================== WELCOME TO THE QUIZ CHALLENGE  (^_^) =====================")
          print("================================================================================")
          print("")
          print("Firstly select the theme you want to take the quiz :-)  ")
          print("")
          print("1. Marvel / DC                     2. Computer Science ")
          print("")
          print("3. General Knowledge               4. Cartoon Animation ")
          print("")
          # after that we have to input a number to initilize the selected theme
          while True:
                    choice = int(input("Enter your choice:- "))
                    # if the choice is wrong then again take the input
                    if(choice > 4 or choice < 1):
                              print("Wrong input kindly enter the valid choice ")
                    if(choice <= 4 and choice >= 1):
                              break
          # if the choice is 1 the quiz based on the Marvel/DC will initialized
          if choice == 1:
                    marvel()
          # if the choice is 2 the quiz based on the Computer science will initialized
          if choice == 2:
                    comsci()
          # if the choice is 3 the quiz based on the General Knowledge will initialized
          if choice == 3:
                    general()
          # if the choice is 1 the quiz based on the Cartoon animation will initialized
          if choice == 4:
                    cartoon()


# It the fuction for general Knowledge
def general():
          # For calculating the last score you get
          score = 0
          # The list take the no of second take the give the answer
          timetaketoans = []
          # The list take the no of question like (1,2,3......)
          question = []
          # It take the question which was created in json file as fil name
          with open("F:\QUIZ_APP_IN_PYTHON_WITH_SOURCE_CODE\Quiz-Application\que\questions.json",'r+') as fil:
              # It load the json file
              j = json.load(fil)
              # Now we have the print 10 question so we use for loop
              for i in range(10):
                        # take the toatl no of question
                        no_of_questions = len(j)
                        # input random question from the json file 
                        ch = random.randint(0, no_of_questions-1)
                        # prints the question
                        print(f'\n Q{i+1} {j[ch]["question"]}\n')
                        # prints the option gien to the question
                        for option in j[ch]["options"]:
                                  print(option)
                        # Now the time starts to answer the question
                        begin = time.time()
                        answer = input("\n Enter your answer: ")
                        # after the input of the answer we end the time
                        time.sleep(1)
                        end = time.time()
                        # Calculate the time taken from end to begin (we take in reverse beacuse end has higher value and it show negative sign)
                        timetaken = int(end - begin)
                        question.append(i+1)
                        timetaketoans.append(timetaken)
                        # Now check the answer you have given it is correct or not
                        if j[ch]["answer"][0] == answer[0].upper():
                                  # it is correct and hence a winning sound is played
                                  print("\n You are correct")
                                  winsound.PlaySound("F:\QUIZ_APP_IN_PYTHON_WITH_SOURCE_CODE\Quiz-Application\que\mixkit-correct-answer-fast-notification-953.wav",winsound.SND_FILENAME)
                                  # Increment the score by one 
                                  score = score + 1
                                  print("=======================================================================================")
                        else:
                                  # the answer is wrong so it played a beep sound by winsound module in python
                                  winsound.Beep(500,500)
                                  print("\n You are incorrect")
                                  print("")
                                  # input the correct answer
                                  print('\n The correct ans is ' + j[ch]["answer"])
                                  print("=======================================================================================")
                        # after that question was removed in order that question woould not repeat again
                        del j[ch]
              print("")
              print("")
              # display the score 
              print("The score is :- " + str(score))
              # it also give reveiw based on your score
              reveiw = comp(score)
              print(reveiw)
              print("")
              # after that if press enter then it will again go to the main menu 
              print("1. Press 'Enter' to go back to the main menu ")
              # afterthat if type ok then graph will appear
              print("2. Enter 'ok' for showing graph report of your answer")
              print("                           OR")
              print("   Press or type anything to exit")
              get = input("Give input for any one of the process:-  ")
              if(get == "" ):
                        main_menu()
              elif(get.upper() == 'OK'):
                        # It will initialised a graph
                        plt.plot(question,timetaketoans,color = "purple",marker = 'o',markerfacecolor ="green",markersize = 10)
                        plt.xlabel("No of Question")
                        plt.ylabel("Time taken to solve the question")
                        plt.title("The accuracy of the question per sec")
                        plt.show()
              else:
                        return

# this function is for the Marvel and DC question
def marvel():
          # For calculating the last score you get
          score = 0
          # The list take the no of second take the give the answer
          timetaketoans = []
          # The list take the no of question like (1,2,3......)
          question = []
          # It take the question which was created in json file as fil name
          with open("F:\sayo\marvel.json",'r+') as fil:
              # It load the json file
              j = json.load(fil)
              # Now we have the print 10 question so we use for loop
              for i in range(10):
                        # take the toatl no of question
                        no_of_questions = len(j)
                        # input random question from the json file 
                        ch = random.randint(0, no_of_questions-1)
                        # prints the question
                        print(f'\n Q{i+1} {j[ch]["question"]}\n')
                        # prints the option gien to the question
                        for option in j[ch]["options"]:
                                  print(option)
                        # Now the time starts to answer the question
                        begin = time.time()
                        answer = input("\n Enter your answer: ")
                        # after the input of the answer we end the time
                        time.sleep(1)
                        end = time.time()
                        # Calculate the time taken from end to begin (we take in reverse beacuse end has higher value and it show negative sign)
                        timetaken = int(end - begin)
                        question.append(i+1)
                        timetaketoans.append(timetaken)
                        # Now check the answer you have given it is correct or not
                        if j[ch]["answer"][0] == answer[0].upper():
                                  # it is correct and hence a winning sound is played
                                  print("\n You are correct")
                                  winsound.PlaySound("F:\QUIZ_APP_IN_PYTHON_WITH_SOURCE_CODE\Quiz-Application\que\mixkit-correct-answer-fast-notification-953.wav",winsound.SND_FILENAME)
                                  # Increment the score by one 
                                  score = score + 1
                                  print("=======================================================================================")
                        else:
                                  # the answer is wrong so it played a beep sound by winsound module in python
                                  winsound.Beep(500,500)
                                  print("\n You are incorrect")
                                  print("")
                                  # input the correct answer
                                  print('\n The correct ans is ' + j[ch]["answer"])
                                  print("=======================================================================================")
                        # after that question was removed in order that question woould not repeat again
                        del j[ch]
              print("")
              print("")
              # display the score 
              print("The score is :- " + str(score))
              # it also give reveiw based on your score
              reveiw = comp(score)
              print(reveiw)
              print("")
              # after that if press enter then it will again go to the main menu 
              print("1. Press 'Enter' to go back to the main menu ")
              # afterthat if type ok then graph will appear
              print("2. Enter 'ok' for showing graph report of your answer")
              print("                           OR")
              print("   Press or type anything to exit")
              get = input("Give input for any one of the process:-  ")
              if(get == "" ):
                        main_menu()
              elif(get.upper() == 'OK'):
                        # It will initialised a graph
                        plt.plot(question,timetaketoans,color = "purple",marker = 'o',markerfacecolor ="green",markersize = 10)
                        plt.xlabel("No of Question")
                        plt.ylabel("Time taken to solve the question")
                        plt.title("The accuracy of the question per sec")
                        plt.show()
              else:
                        return
                    

def comsci():
          # For calculating the last score you get
          score = 0
          # The list take the no of second take the give the answer
          timetaketoans = []
          # The list take the no of question like (1,2,3......)
          question = []
          # It take the question which was created in json file as fil name
          with open("F:\sayo\comsci.json",'r+') as fil:
              # It load the json file
              j = json.load(fil)
              # Now we have the print 10 question so we use for loop
              for i in range(10):
                        # take the toatl no of question
                        no_of_questions = len(j)
                        # input random question from the json file 
                        ch = random.randint(0, no_of_questions-1)
                        # prints the question
                        print(f'\n Q{i+1} {j[ch]["question"]}\n')
                        # prints the option gien to the question
                        for option in j[ch]["options"]:
                                  print(option)
                        # Now the time starts to answer the question
                        begin = time.time()
                        answer = input("\n Enter your answer: ")
                        # after the input of the answer we end the time
                        time.sleep(1)
                        end = time.time()
                        # Calculate the time taken from end to begin (we take in reverse beacuse end has higher value and it show negative sign)
                        timetaken = int(end - begin)
                        question.append(i+1)
                        timetaketoans.append(timetaken)
                        # Now check the answer you have given it is correct or not
                        if j[ch]["answer"][0] == answer[0].upper():
                                  # it is correct and hence a winning sound is played
                                  print("\n You are correct")
                                  winsound.PlaySound("F:\QUIZ_APP_IN_PYTHON_WITH_SOURCE_CODE\Quiz-Application\que\mixkit-correct-answer-fast-notification-953.wav",winsound.SND_FILENAME)
                                  # Increment the score by one 
                                  score = score + 1
                                  print("=======================================================================================")
                        else:
                                  # the answer is wrong so it played a beep sound by winsound module in python
                                  winsound.Beep(500,500)
                                  print("\n You are incorrect")
                                  print("")
                                  # input the correct answer
                                  print('\n The correct ans is ' + j[ch]["answer"])
                                  print("=======================================================================================")
                        # after that question was removed in order that question woould not repeat again
                        del j[ch]
              print("")
              print("")
              # display the score 
              print("The score is :- " + str(score))
              # it also give reveiw based on your score
              reveiw = comp(score)
              print(reveiw)
              print("")
              # after that if press enter then it will again go to the main menu 
              print("1. Press 'Enter' to go back to the main menu ")
              # afterthat if type ok then graph will appear
              print("2. Enter 'ok' for showing graph report of your answer")
              print("                           OR")
              print("   Press or type anything to exit")
              get = input("Give input for any one of the process:-  ")
              if(get == "" ):
                        main_menu()
              elif(get.upper() == 'OK'):
                        # It will initialised a graph
                        plt.plot(question,timetaketoans,color = "purple",marker = 'o',markerfacecolor ="green",markersize = 10)
                        plt.xlabel("No of Question")
                        plt.ylabel("Time taken to solve the question")
                        plt.title("The accuracy of the question per sec")
                        plt.show()
              else:
                        return


def cartoon():
          # For calculating the last score you get
          score = 0
          # The list take the no of second take the give the answer
          timetaketoans = []
          # The list take the no of question like (1,2,3......)
          question = []
          # It take the question which was created in json file as fil name
          with open("F:\sayo\cartton.json",'r+') as fil:
              # It load the json file
              j = json.load(fil)
              # Now we have the print 10 question so we use for loop
              for i in range(10):
                        # take the toatl no of question
                        no_of_questions = len(j)
                        # input random question from the json file 
                        ch = random.randint(0, no_of_questions-1)
                        # prints the question
                        print(f'\n Q{i+1} {j[ch]["question"]}\n')
                        # prints the option gien to the question
                        for option in j[ch]["options"]:
                                  print(option)
                        # Now the time starts to answer the question
                        begin = time.time()
                        answer = input("\n Enter your answer: ")
                        # after the input of the answer we end the time
                        time.sleep(1)
                        end = time.time()
                        # Calculate the time taken from end to begin (we take in reverse beacuse end has higher value and it show negative sign)
                        timetaken = int(end - begin)
                        question.append(i+1)
                        timetaketoans.append(timetaken)
                        # Now check the answer you have given it is correct or not
                        if j[ch]["answer"][0] == answer[0].upper():
                                  # it is correct and hence a winning sound is played
                                  print("\n You are correct")
                                  winsound.PlaySound("F:\QUIZ_APP_IN_PYTHON_WITH_SOURCE_CODE\Quiz-Application\que\mixkit-correct-answer-fast-notification-953.wav",winsound.SND_FILENAME)
                                  # Increment the score by one 
                                  score = score + 1
                                  print("=======================================================================================")
                        else:
                                  # the answer is wrong so it played a beep sound by winsound module in python
                                  winsound.Beep(500,500)
                                  print("\n You are incorrect")
                                  print("")
                                  # input the correct answer
                                  print('\n The correct ans is ' + j[ch]["answer"])
                                  print("=======================================================================================")
                        # after that question was removed in order that question woould not repeat again
                        del j[ch]
              print("")
              print("")
              # display the score 
              print("The score is :- " + str(score))
              # it also give reveiw based on your score
              reveiw = comp(score)
              print(reveiw)
              print("")
              # after that if press enter then it will again go to the main menu 
              print("1. Press 'Enter' to go back to the main menu ")
              # afterthat if type ok then graph will appear
              print("2. Enter 'ok' for showing graph report of your answer")
              print("                           OR")
              print("   Press or type anything to exit")
              get = input("Give input for any one of the process:-  ")
              if(get == "" ):
                        main_menu()
              elif(get.upper() == 'OK'):
                        # It will initialised a graph
                        plt.plot(question,timetaketoans,color = "purple",marker = 'o',markerfacecolor ="green",markersize = 10)
                        plt.xlabel("No of Question")
                        plt.ylabel("Time taken to solve the question")
                        plt.title("The accuracy of the question per sec")
                        plt.show()
              else:
                        return

# it is for reveiw the score 
def comp(score):
          # if the score is less than equal to the 5 then it show...
          if(score <= 5):
                    print("Its okk better luck next time.")
           #  if the score is above 5 and less than equal to the 7 then 
          elif(score > 5 and score <=7):
                    print("You are preety good in this field.")
            # i fthe score is above 7 then it show ...
          elif(score > 7):
                    print("Perfect!!! Tou are damm good ^_^")

if __name__ == '__main__':
          main()
          
