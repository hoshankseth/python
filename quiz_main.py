from question_model import Question
from data import question_data
from quiz_brainer import QuizBrain
import random

ques = []
for q in question_data:
    question_text = q['text']
    question_ans = q['answer']
    question = Question(question_text, question_ans)
    ques.append(question)

quiz = QuizBrain(ques)

while quiz.still_has_questions():
    quiz.next_question()

print(f"Your quiz is completed")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")

