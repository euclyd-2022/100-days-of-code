from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    #only pass quizbrain object of datatype QuizBrain
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(background=THEME_COLOR, padx=20, pady=20)


        self.text_area = Canvas(height=250, width=300, bg="white")
        self.question_text = self.text_area.create_text(150, 125, text="Question no.1", fill=THEME_COLOR, font=("Arial", 20, "italic"), width=280)
        self.text_area.grid(column=0, row=1, columnspan=2, pady=50)


        self.score = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        # no self. as it won't need accessing from elswehere in the class
        tick_img = PhotoImage(file="images/true.png")
        self.tick_button = Button(image=tick_img, command=self.true_pressed)
        self.tick_button.grid(column=0, row=2)

        cross_img = PhotoImage(file="images/false.png")
        self.cross_button = Button(image=cross_img, command=self.false_pressed)
        self.cross_button.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.text_area.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.text_area.itemconfig(self.question_text, text=q_text)
        else:
            q_text = "You've reached the end of the quiz!"
            self.text_area.itemconfig(self.question_text, text=q_text)
            self.tick_button.config(state="disabled")
            self.cross_button.config(state="disabled")


    def true_pressed(self):
       is_right = self.quiz.check_answer("True")
       self.give_feedback(is_right)


    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.text_area.configure(bg="green")
        else:
            self.text_area.configure(bg="red")

        self.window.after(1000, self.get_next_question)


