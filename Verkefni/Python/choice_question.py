from question import Question

class ChoiceQuestion(Question):
    def __init__(self, __question_str, __answer_str=0) -> None:
        super().__init__(__question_str, __answer_str)
        self.__question_str = __question_str
        self.__question_list = []
        self.answer_index = 0
        

    def add_choice(self, choice: str, answer: bool):
        self.__question_list.append([choice, answer])
        if answer == True:
            self.answer_index = len(self.__question_list)

    def check_answer(self, answer) -> bool:
        if str(answer).isnumeric():
            if int(answer) == int(self.answer_index):
                return True
        return False
    
    def get_question(self):
        return_value = "" 
        return_value += self.__question_str + "\n"
        for i in range(len(self.__question_list)):
            if i == 0:
                return_value += "{}. {}".format(i+1, self.__question_list[i][0])
            else:
                return_value += "\n{}. {}".format(i+1, self.__question_list[i][0])
        return return_value

    
    def __str__(self) -> str:
        return "Q: {} A: {}".format(self.__question_str, self.answer_index)
    
    def __repr__(self) -> str:
        return "Question: {} Answer: {}".format(self.__question_str, self.answer_index)






