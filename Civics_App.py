import random
import tkinter as tk
from tkinter import messagebox

# 1. THE DATA CARGO (You can keep adding your 128 here)
# Format: {"q": "Question", "a": "Correct Answer"}
quiz_data = [
    {"q": "Who is the Vice President now?", "a": "JD Vance"},
    {"q": "Who is the Secretary of War now?", "a": "Pete Hegseth"},
    {"q": "What is the capital of the US?", "a": "Washington DC"},
    {"q": "Who is the Speaker of the House?", "a": "Mike Johnson"},
    # Comrade, just keep pasting your typed questions here!
]

class SovereignQuizzer:
    def __init__(self, root):
        self.root = root
        random.shuffle(quiz_data)
        self.root.title("Sovereign Civics Master 2026")
        self.root.geometry("600x450")
        self.root.configure(bg="#2c3e50") # Dark professional background

        self.current_index = 0
        self.score = 0

        # UI Elements
        self.title_label = tk.Label(root, text="N-400 MISSION CONTROL", font=("Courier", 20, "bold"), fg="#ecf0f1", bg="#2c3e50")
        self.title_label.pack(pady=20)

        self.question_label = tk.Label(root, text="", font=("Arial", 14), fg="white", bg="#2c3e50", wraplength=500)
        self.question_label.pack(pady=20)

        self.entry = tk.Entry(root, font=("Arial", 16), justify="center")
        self.entry.pack(pady=10)
        self.entry.bind('<Return>', lambda event: self.check_answer()) # Press 'Enter' to submit!

        self.submit_btn = tk.Button(root, text="VALIDATE LOGIC", command=self.check_answer, font=("Arial", 12, "bold"), bg="#27ae60", fg="white", width=20)
        self.submit_btn.pack(pady=20)

        self.status_label = tk.Label(root, text="", font=("Arial", 12), fg="#f1c40f", bg="#2c3e50")
        self.status_label.pack(side="bottom", pady=20)

        self.load_question()

    def load_question(self):
        if self.current_index < len(quiz_data):
            q_text = quiz_data[self.current_index]["q"]
            self.question_label.config(text=f"QUESTION {self.current_index + 1}: \n{q_text}")
            self.entry.delete(0, tk.END)
            self.update_status()
        else:
            messagebox.showinfo("Mission Success", f"FINAL SCORE: {self.score}/{len(quiz_data)}\n\nYou are ready for the Department of War!")
            self.root.destroy()

    def update_status(self):
        self.status_label.config(text=f"PROGRESS: {self.current_index}/{len(quiz_data)}  |  SCORE: {self.score}")

    def check_answer(self):
        user_ans = self.entry.get().strip().lower()
        correct_ans = quiz_data[self.current_index]["a"].lower()

        # Logic check: We use 'in' so if the answer is "Washington DC" and you type "Washington", it counts!
        if user_ans in correct_ans or correct_ans in user_ans:
            self.score += 1
            messagebox.showinfo("SUCCESS", "Variable Verified. Correct!")
        else:
            messagebox.showerror("GLITCH DETECTED", f"Incorrect. System requires: {quiz_data[self.current_index]['a']}")
        
        self.current_index += 1
        self.load_question()

# Ignition
if __name__ == "__main__":
    root = tk.Tk()
    app = SovereignQuizzer(root)
    root.mainloop()