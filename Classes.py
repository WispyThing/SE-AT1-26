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

        global score
        score = score + self.__points
        
        print(f"Your new score is {score}.")


    def askQuestion(self):
        while True:
            self.answer = input(f"Question {self.number}. {self.words} ")
                
            if self.answer in ["yes", "no"]:
                if self.answer == self.__correct_answer:
                    print("Correct!")
                    self.addPoints()
                else:
                    print("Incorrect.")
                return self.answer
            else:
                print("Invalid input. Please type 'yes' or 'no'.")
            
    
class Minigames(Questions):
    
    def __init__(self, mini_number, words, answer, correct_answer,):

        super().__init__(mini_number, words, answer, correct_answer, 10)

        self.mini_number = mini_number


    def askQuestion(self):
        while True:
            self.answer = input(f"You've encountered minigame {self.mini_number}! {self.words} ")
                
            if self.answer in ["yes", "no"]:
                if self.answer == self.__correct_answer:
                    print("Correct!")
                    self.addPoints()
                else:
                    print("Incorrect.")
                return self.answer
            else:
                print("Invalid input. Please type 'yes' or 'no'.")
    

    def addPoints(self):

        global score
        score = score + 10
        
        print(f"Your new score is {score}.")

    def minigameSelection(self):

        minigame_chosen = random.randint(1, 5)

        if minigame_chosen == 1:
            Minigame1.askQuestion()
        elif minigame_chosen == 2:
            Minigame2.askQuestion()
        elif minigame_chosen == 3:
            Minigame3.askQuestion()
        elif minigame_chosen == 4:
            Minigame4.askQuestion()
        elif minigame_chosen == 5:
            Minigame5.askQuestion()

    

Question1 = Questions(1, "You have a test coming up, do you study the days before the test?", "", "yes", 25)
Question2 = Questions(2, "Your test is tomorrow! Do you sleep in the night before the test?", "", "yes", 25)
Question3 = Questions(3, "It's the day of the test! Your friend tells you to cheat on the test, do you cheat?", "", "no", 50)

Minigame1 = Minigames(1, "", "", "")
Minigame2 = Minigames(2, "", "", "")
Minigame3 = Minigames(3, "", "", "")
Minigame4 = Minigames(4, "", "", "")
Minigame5 = Minigames(5, "", "", "")

