class Question:
    def __init__(self,  __question_str, __answer_str) -> None:
        self.__question_str = __question_str
        self.__answer_str = __answer_str
    
    def get_question(self):
        return self.__question_str
 

    def check_answer(self, answer: str) -> bool:
        if self.__answer_str.lower() == answer.lower():
            return True
        return False
    
    
    def __str__(self) -> str:
        return "Q: {} A: {}".format(self.__question_str, self.__answer_str)
    
    def __repr__(self) -> str:
        return "Question: {} Answer: {}".format(self.__question_str, self.__answer_str)

