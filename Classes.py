score = 0

class Question:
    def __init__(self, number, words, answer, correct_answer, points):

        self.number = number

        self.words = words

        self.answer = answer

        self.__correct_answer = correct_answer

        self.__points = points

    def getPoints(self):
        return self.__points

    def setPoints(self, points):

        if points > 0:
            self.__points = points

    def getCorrectAnswer(self):
        return self.__correct_answer

    def setCorrectAnswer(self, correct_answer):
        self.__correct_answer = correct_answer

    def addPoints(self):

        score = score + self.__points
        
        print(f"Your new score is {score}.")


    def askQuestions(self):
        while True:
            self.answer = input(f"Question {self.number}. {self.words} ")
                
            if self.answer in ["yes", "no"]:
                return self.answer
            else:
                print("Invalid input. Please type 'yes' or 'no'.")
    