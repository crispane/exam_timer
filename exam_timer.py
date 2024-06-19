import tkinter as tk
from tkinter import simpledialog

class ExamTimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Exam Timer")

        self.total_time = 0
        self.question_time = 0
        self.time_pool = 0
        self.remaining_total_time = 0
        self.remaining_question_time = 0
        self.questions_count = 0

        self.total_time_label = tk.Label(root, text="Total Time: 00:00:00")
        self.total_time_label.pack()

        self.question_time_label = tk.Label(root, text="Question Time: 00:00")
        self.question_time_label.pack()

        self.time_pool_label = tk.Label(root, text="Time Pool: 00:00")
        self.time_pool_label.pack()

        self.questions_count_label = tk.Label(root, text="Question: 0")
        self.questions_count_label.pack()

        self.start_button = tk.Button(root, text="Start Exam", command=self.start_exam)
        self.start_button.pack()

        self.next_question_button = tk.Button(root, text="Next Question", command=self.next_question, state=tk.DISABLED)
        self.next_question_button.pack()

        self.timer_running = False

    def start_exam(self):
        self.questions_count += 1
        self.questions_count_label.config(text=f"Question: 1")
        self.total_time = simpledialog.askinteger("Input", "Enter total time (minutes):", minvalue=1)
        self.question_time = simpledialog.askinteger("Input", "Enter question time (seconds):", minvalue=1)

        self.remaining_total_time = self.total_time * 60
        self.remaining_question_time = self.question_time

        self.start_button.config(state=tk.DISABLED)
        self.next_question_button.config(state=tk.NORMAL)
        self.timer_running = True
        self.update_timers()

    def next_question(self):
        self.questions_count += 1
        self.questions_count_label.config(text=f"Question: {self.questions_count}")

        self.time_pool += self.remaining_question_time
        self.remaining_question_time = self.question_time
        self.update_time_pool_label()

    def update_timers(self):
        if self.timer_running:
            if self.remaining_total_time > 0:
                self.remaining_total_time -= 1
                self.update_total_time_label()

                if self.remaining_question_time > 0:
                    self.remaining_question_time -= 1
                else:
#                    if self.time_pool > 0:
#                        self.time_pool -= 1
#                    else:
                    self.time_pool -= 1
                    self.update_time_pool_label()

                self.update_question_time_label()
                self.root.after(1000, self.update_timers)
            else:
                self.timer_running = False
                self.start_button.config(state=tk.NORMAL)
                self.next_question_button.config(state=tk.DISABLED)

    def update_total_time_label(self):
        mins, secs = divmod(self.remaining_total_time, 60)
        hours, mins = divmod(mins, 60)
        self.total_time_label.config(text=f"Total Time: {hours:02d}:{mins:02d}:{secs:02d}")

    def update_question_time_label(self):
        mins, secs = divmod(self.remaining_question_time, 60)
        self.question_time_label.config(text=f"Question Time: {mins:02d}:{secs:02d}")

    def update_time_pool_label(self):
        mins, secs = divmod(abs(self.time_pool), 60)
        sign = "-" if self.time_pool < 0 else ""
        self.time_pool_label.config(text=f"Time Pool: {sign}{mins:02d}:{secs:02d}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExamTimerApp(root)
    root.mainloop()
