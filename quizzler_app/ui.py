from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg='white')
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 100,
                                                     width=290,
                                                     text="This is the question",
                                                     font=('Arial', 15, 'italic'),
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, bg=THEME_COLOR, command=self.choose_true)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, bg=THEME_COLOR, command=self.choose_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
        self.enable_button()
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You've reached to the end of the quiz\n"
                                        f"Your final score is: {self.quiz.score}/{self.quiz.question_number}")
            self.disable_button()

    def choose_true(self):
        self.disable_button()
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def choose_false(self):
        self.disable_button()
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg='green')
            self.canvas.itemconfig(self.question_text, fill="white")
        else:
            self.canvas.config(bg='red')
            self.canvas.itemconfig(self.question_text, fill="white")

        self.window.after(1000, self.get_next_question)

    def enable_button(self):
        self.true_button.config(state='active')
        self.false_button.config(state='active')

    def disable_button(self):
        self.true_button.config(state='disabled')
        self.false_button.config(state='disabled')
