import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

student_scores = {student:random.randint(1,100) for student in names}

print(student_scores)

passed_students = {student:score for (student, score) in student_scores.items() if score >= 60  }

print(passed_students)

sentence_inp = "What is the Airspeed Velocity of an Unladen Swallow?"

sentence_list = [sentence_inp.split()]

#print(sentence_inp.split)

import calendar

days_of_the_week = list(calendar.day_name)
print(days_of_the_week)

dict_sentence = {word:len(word) for word in sentence_inp.split()}
print(dict_sentence)