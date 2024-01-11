from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    q = Question(question["question"], question["correct_answer"]) # Be careful not to lose the object functionality or else, the
    # object will not allow access to methods and it's variables if you want to use it later down the line.
    question_bank.append(q)

# print(question_bank)

quiz_set = QuizBrain(question_bank)
# print(quiz_set.question_list)

while quiz_set.still_has_questions():
    quiz_set.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz_set.score}/{quiz_set.question_number}")
