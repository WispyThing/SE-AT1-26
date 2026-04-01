import random

score = 0

minigame_chosen = 0

class Questions:
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


    def askQuestion(self):
        while True:
            self.answer = input(f"Question {self.number}. {self.words} ")
                
            if self.answer in ["yes", "no"]:
                return self.answer
            else:
                print("Invalid input. Please type 'yes' or 'no'.")
    
class Minigames(Questions):
    
    def __init__(self, mini_number, words, answer, correct_answer):

        super().__init__(words, answer, correct_answer)

        self.mini_number = mini_number


    def askQuestion(self):
        while True:
            self.answer = input(f"You've encountered minigame {self.mini_number}! {self.words} ")
                
            if self.answer in ["yes", "no"]:
                return self.answer
            else:
                print("Invalid input. Please type 'yes' or 'no'.")
    

    def addPoints(self):

        score = score + 10
        
        print(f"Your new score is {score}.")

    def minigameSelection(self):

        minigame_chosen = random.randint(1,2,3,4,5)

        match minigame_chosen:
            case(1):
                Minigame1.askQuestion()
            case(2):
                Minigame2.askQuestion()
            case(3):
                Minigame3.askQuestion()
            case(4):
                Minigame4.askQuestion()
            case(5):
                Minigame5.askQuestion()

    

Question1 = Questions(1, "", "", "", 25)
Question2 = Questions(2, "", "", "", 25)
Question3 = Questions(3, "", "", "", 50)

Minigame1 = Minigames(1, "", "", "")
Minigame2 = Minigames(2, "", "", "")
Minigame3 = Minigames(3, "", "", "")
Minigame4 = Minigames(4, "", "", "")
Minigame5 = Minigames(5, "", "", "")

