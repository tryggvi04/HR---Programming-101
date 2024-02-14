from question import Question
from choice_question import ChoiceQuestion

class Exam:
    def __init__(self) -> None:
        self.question_list = []
        self.points = 0

    def add_question(self, question: Question):
        self.question_list.append(question)

    def get_points(self):
        return self.points
    
    def get_num_questions(self):
        return len(self.question_list)
    
    def take(self):
        for question in self.question_list:
             print(question.get_question())
             response = input()
             print("{}{}".format(question.check_answer(response), "\n"))

             if question.check_answer(response):
                 self.points += 1
    
    def __str__(self) -> str:
        return "\n".join(map(str, self.question_list))
    

