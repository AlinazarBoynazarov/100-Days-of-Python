class QuizBrain:


    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        choice = input(f"Q.{self.question_number}: {current_question.text} (True/False) ")
        self.check_answer(choice, current_question)
        
        
    def check_answer(self, choice, current_question):

        if choice.lower() == current_question.answer.lower():
            print("You got it right!")
            self.score += 1
            print(f"The correct answer was: {current_question.answer}")
            print(f"Your current score is: {self.score}/{self.question_number}")
            print("\n")
        
        else:
            print("That's wrong.")
            print(f"The correct answer was: {current_question.answer}")
            print(f"Your current score is: {self.score}/{self.question_number}")
            print("\n")
            

    def still_has_question(self):
        if self.question_number != len(self.question_list):
            return True
        elif self.question_number == len(self.question_list):
            print(f"You've completed the quiz")
            print(f"Your final score was: {self.score}/{self.question_number}")
            return False


        


    

















    # def __init__(self, q_list):
    #     self.question_number = 0
    #     self.question_list = q_list

    
    # def next_question(self):
    #     current_question = self.question_list[self.question_number]
    #     self.question_number += 1
    #     choice = input(f"Q.{self.question_number}: {current_question.text} (True/False) ")
        

    # def still_has_question(self):
    #     if self.question_number == 12: 
    #         return False
    #     else:
    #         return True
        

        # if choice == current_question.answer:
        #     return True
        # elif choice != current_question.answer:
        #     return False





        

        
