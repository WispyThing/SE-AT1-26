import random

score = 0

class Questions:
    def __init__(self, number, words, answer, correct_answer, feedback, points):

        self.number = number

        self.words = words

        self.answer = answer

        self.__correct_answer = correct_answer

        self.feedback = feedback

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
        score += self.__points
        
        print(f"Your new score is {score}.")


    def askQuestion(self):
        while True:
            self.answer = input(f"Question {self.number}. {self.words} ").lower()
            
                
            if self.answer in ["yes", "no"]:
                if self.answer == self.__correct_answer:
                    print("")
                    print("Correct!")
                    print("")
                    self.addPoints()
                    print("")
                else:
                    print("")
                    print("Incorrect.")
                    print("")
                    print(f"Here is some feedback! {self.feedback}")
                    print("")
                return self.answer
            else:
                print("Invalid input. Please type 'yes' or 'no'.")
            
    
class Minigames(Questions):
    
    def __init__(self, number, words, answer, correct_answer, feedback):

        super().__init__(number, words, answer, correct_answer, feedback, 10)



    def askQuestion(self):
        while True:
            self.answer = input(f"You've encountered minigame {self.number}! {self.words} ").lower()
                
            if self.answer in ["yes", "no"]:
                if self.answer == self.getCorrectAnswer():
                    print("")
                    print("Correct!")
                    print("")
                    self.addPoints()
                    print("")
                else:
                    print("")
                    print("Incorrect.")
                    print("")
                    print(f"Here is some feedback! {self.feedback}")
                    print("")
                return self.answer
            else:
                print("Invalid input. Please type 'yes' or 'no'.")
    

    def addPoints(self):

        global score
        score += 10
        
        print(f"Your new score is {score}.")


def minigameSelection():

    global available_minigames
    chosen = random.choice(available_minigames)
    available_minigames.remove(chosen)
    chosen.askQuestion()

Question1 = Questions(1, "You have a test coming up, do you study the days before the test?", "", "yes", "It's always important to study before a test to ensure you know your content!", 25)
Question2 = Questions(2, "Your test is tomorrow! Do you sleep in the night before the test?", "", "yes", "Good rest before a test is important as it improves your cognitive function on the day of the test!", 25)
Question3 = Questions(3, "It's the day of the test! Your friend tells you to cheat on the test, do you cheat?", "", "no", "Never cheat on a test! If you get caught it is often an instant zero! Hard work will always beat cheating!", 50)

Minigame1 = Minigames(1, "You see an old lady waiting to cross a road, do you help her?", "", "yes", "Make sure to always help people around you when they look like they need help!")
Minigame2 = Minigames(2, "You have homework due soon! Do you ditch it to hang out with your friends?", "", "no", "While hanging out with your friends and making memories is always important, you need to make sure you are always caught up on schoolwork! It is ok to take breaks every now and again though!.")
Minigame3 = Minigames(3, "You're impatient waiting in line in the canteen, do you skip to the front of the line?", "", "no", "If everyone else is waiting patiently, don't cut in, respect their time as much as yours!")
Minigame4 = Minigames(4, "Your mate wants you to skip class, do you tag along?", "", "no", "Skipping even one class can set you very behind in your learning! It is important that you attend all of your classes when you are able to!")
Minigame5 = Minigames(5, "You have a question for your teacher but you aren't sure on whether you should ask it or not, do you ask it?", "", "yes", "It is always important to ask quesitons when you are unsure of something, there are no stupid questions!")

available_minigames = [Minigame1, Minigame2, Minigame3, Minigame4, Minigame5]
