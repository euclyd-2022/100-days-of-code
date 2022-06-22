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


        self.text_area = Canvas(height=250, width=300)
        self.question_text = self.text_area.create_text(150, 125, text="Question no.1", fill=THEME_COLOR, font=("Arial", 20, "italic"), width=280)
        self.text_area.grid(column=0, row=1, columnspan=2, pady=50)


        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        # no self. as it won't need accessing from elswehere in the class
        tick_img = PhotoImage(file="images/true.png")
        tick_button = Button(image=tick_img)
        tick_button.grid(column=0, row=2)

        cross_img = PhotoImage(file="images/false.png")
        cross_button = Button(image=cross_img)
        cross_button.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.text_area.itemconfig(self.question_text, text=q_text)

