from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz_brain = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_text = Label(text=f"Score : {self.quiz_brain.score}", fg="white", bg=THEME_COLOR)
        self.score_text.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.quiz_text = self.canvas.create_text(
            150, 125, width=280 ,text="Some Question", font=("Arial", 20, "italic"), fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="00_projects/26_quizzler_app/images/true.png")
        self.true_btn = Button(image=(true_img), highlightthickness=0, command=self.check_answer_true)
        self.true_btn.grid(row=2, column=0)

        false_img = PhotoImage(file="00_projects/26_quizzler_app/images/false.png")
        self.false_btn = Button(image=(false_img), highlightthickness=0, command=self.check_answer_false)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            question = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.quiz_text, text=question)
        else:
            self.canvas.itemconfig(self.quiz_text, text="You've reached the end of the questions")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")


    def check_answer_false(self):
        self.give_feedback(self.quiz_brain.check_answer("false"))

    def check_answer_true(self):        
        self.give_feedback(self.quiz_brain.check_answer("true"))
        

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score_text.config(text=f"Score : {self.quiz_brain.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)