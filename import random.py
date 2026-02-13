import random
import tkinter as tk
from tkinter import messagebox

# 1. THE DATA CARGO
quiz_data = [
    {"q": "Who is the Vice President now?", "a": "JD Vance"},
    {"q": "Who is the Secretary of War now?", "a": "Pete Hegseth"},
    {"q": "What is the capital of the US?", "a": "Washington DC"},
    {"q": "Who is the Speaker of the House?", "a": "Mike Johnson"},
    {"q": "What is the supreme law of the land?", "a": "The Constitution"},
    {"q": "Who is one of your state's U.S. Senators now?", "a": "Chris Van Hollan"},
    {"q": "The House of Representatives has how many voting members?", "a": "435"},
    {"q": "We elect a U.S. Representative for how many years?", "a": "2"},
    {"q": "Name your U.S. Representative.", "a": "Jamie Raskin"},
    {"q": "Who does a U.S. Senator represent?", "a": "All people of the state"},
    {"q": "Why do some states have more Representatives than other states?", "a": "Because of the state's population"},
    {"q": "We elect a President for how many years?", "a": "4"},
    {"q": "In what month do we vote for President?", "a": "November"},
    {"q": "What is the name of the President of the United States now?", "a": "Donald Trump"},
    {"q": "If the President can no longer serve, who becomes President?", "a": "The Vice President"},
    {"q": "If both the President and the Vice President can no longer serve, who becomes President?", "a": "The Speaker of the House"},
    {"q": "Who is the Commander in Chief of the military?", "a": "The President"},
    {"q": "Who signs bills to become laws?", "a": "The President"},
    {"q": "Who vetoes bills?", "a": "The President"},
    {"q": "What does the President’s Cabinet do?", "a": "Advises the President"},
    {"q": "What are two Cabinet-level positions?", "a": "Secretary of State and Secretary of Defense"},
    {"q": "What does the judicial branch do?", "a": "Reviews laws"},
    {"q": "What is the highest court in the United States?", "a": "The Supreme Court"},
    {"q": "How many justices are on the Supreme Court?", "a": "9"},
    {"q": "Who is the Chief Justice of the United States now?", "a": "John Roberts"},
    {"q": "Under our Constitution, some powers belong to the federal government. What is one power of the federal government?", "a": "To print money"},
    {"q": "Under our Constitution, some powers belong to the states. What is one power of the states?", "a": "Provide schooling and education"},
    {"q": "Who is the Governor of your state now?", "a": "Answers will vary"},
    {"q": "What is the capital of your state?", "a": "Answers will vary"},
    {"q": "What are the two major political parties in the United States?", "a": "Democratic and Republican"},
    {"q": "What is the political party of the President now?", "a": "Republican Party"},
    {"q": "What is the name of the Speaker of the House of Representatives now?", "a": "Mike Johnson"},
    {"q": "There are four amendments to the Constitution about who can vote. Describe one of them.", "a": "Citizens 18 and older can vote"},
    {"q": "What is one responsibility that is only for United States citizens?", "a": "Serve on a jury"},
    {"q": "Name one right only for United States citizens.", "a": "Vote in a federal election"},
    {"q":  "What is Veterans Day.", "a": "A holiday to honor people who have served (in the U.S. military)"},
    {"q": "What does the judicial branch do?", "a": "Explains laws"},
    {"q": "What is the highest court in the United States?", "a": "The Supreme Court"},
    {"q": "How many justices are on the Supreme Court?", "a": "9"},
    {"q": "Who is the Chief Justice of the United States now?", "a": "John Roberts"},
    {"q": "Under our Constitution, some powers belong to the federal government. What is one power of the federal government?", "a": "To print money"},
    {"q": "Under our Constitution, some powers belong to the states. What is one power of the states?", "a": "Provide schooling and education"},
    {"q": "What is the capital of Maryland?", "a": "Annapolis"},
    {"q": "What are the two major political parties in the United States?", "a": "Democratic and Republican"},
    {"q": "What is the political party of the President now?", "a": "Republican"},
    {"q": "There are four amendments to the Constitution about who can vote. Describe one of them.", "a": "Citizens 18 and older can vote"},
    {"q": "When is the last day you can send in federal income tax forms?", "a": "April 15"},
    {"q": "When must all men register for the Selective Service?", "a": "At age 18"},
    {"q": "What is one reason colonists came to America?", "a": "Freedom"},
    {"q": "Who lived in America before the Europeans arrived?", "a": "American Indians"},
    {"q": "Name two national U.S. holidays.", "a": "Memorial Day and Veterans Day"},
    {"q": "What group of people was taken to America and sold as slaves?", "a": "Africans"},
    {"q": "Why did the colonists fight the British?", "a": "Because of high taxes"},
    {"q": "Who wrote the Declaration of Independence?", "a": "Thomas Jefferson"},
    {"q": "When was the Declaration of Independence adopted?", "a": "July 4, 1776"},
    {"q": "There were 13 original states. Name three.", "a": "New York, New Jersey, and Pennsylvania"},
    {"q": "What happened at the Constitutional Convention?", "a": "The Constitution was written"},
    {"q": "When was the Constitution written?", "a": "1787"},
    {"q": "The Federalist Papers supported the passage of the U.S. Constitution. Name one of the writers.", "a": "James Madison"},
    {"q": "What is one thing Benjamin Franklin is famous for?", "a": "U.S. diplomat"},
    {"q": "Who is the 'Father of Our Country'?", "a": "George Washington"},
    {"q": "What territory did the United States buy from France in 1803?", "a": "Louisiana"},
    {"q": "Name one war fought by the United States in the 1800s.", "a": "Civil War"},
    {"q": "Name the U.S. war between the North and the South.", "a": "the Civil War"},
    {"q": "Name one problem that led to the Civil War.", "a": "Slavery"},
    {"q": "What was one important thing that Abraham Lincoln did?", "a": "Freed the slaves"},
    {"q": "What did Susan B. Anthony do?", "a": "Fought for women's rights"},
    {"q": "Name one war fought by the United States in the 1900s.", "a": "World War I"},
    {"q": "Who was President during World War I?", "a": "Woodrow Wilson"},
    {"q": "Who was President during the Great Depression and World War II?", "a": "Franklin Roosevelt"},
    {"q": "Who did the United States fight in World War II?", "a": "Japan, Germany, and Italy"},
    {"q": "During the Cold War, what was the main concern of the United States?", "a": "Communism"},
    {"q": "What movement tried to end racial discrimination?", "a": "Civil rights movement"},
    {"q": "What did Martin Luther King, Jr. do?", "a": "Fought for civil rights"},
    {"q": "What major event happened on September 11, 2001, in the United States?", "a": "Terrorists attacked the United States"},
    {"q": "Name one American Indian tribe in the United States.", "a": "Cherokee"},
    {"q": "Name one of the two longest rivers in the United States.", "a": "Mississippi River"},
    {"q": "What ocean is on the West Coast of the United States?", "a": "Pacific Ocean"},
    {"q": "What ocean is on the East Coast of the United States?", "a": "Atlantic Ocean"},
    {"q": "Name one U.S. territory.", "a": "Puerto Rico"},
    {"q": "Name one state that borders Canada.", "a": "New York"},
    {"q": "Name one state that borders Mexico.", "a": "Texas"},
    {"q": "What is the capital of the United States?", "a": "Washington, D.C."},
    {"q": "Where is the Statue of Liberty?", "a": "New York Harbor"},
    {"q": "Why does the flag have 13 stripes?", "a": "Because there were 13 original colonies"},
    {"q": "Why does the flag have 50 stars?", "a": "Because there is one star for each state"},
    {"q": "What is the name of the national anthem?", "a": "The Star-Spangled Banner"},
    {"q": "When do we celebrate Independence Day?", "a": "July 4"},
    {"q": "Name two national U.S. holidays.", "a": "Christmas and Thanksgiving"},
    {"q": "What is the motto of the United States?", "a": "In God We Trust"},
    {"q": "What is the name of the President of the United States now?", "a": "Donald Trump"},
    {"q": "How many amendments does the Constitution have?", "a": "27"},
    {"q": "Who is in charge of the executive branch?", "a": "The President"},
    {"q": "What are two parts of the U.S. Congress?", "a": "The Senate and House"},
    {"q": "Why do some states have more Representatives than other states?", "a": "Because of the state's population"},
    {"q": "We elect a U.S. Senator for how many years?", "a": "6"},
    {"q": "What does the President’s Cabinet do?", "a": "Advises the President"},
    {"q": "What are two Cabinet-level positions?", "a": "Secretary of State and Secretary of Labor"},
    {"q": "If the President can no longer serve, who becomes President?", "a": "The Vice President"},
    {"q": "If both the President and the Vice President can no longer serve, who becomes President?", "a": "The Speaker of the House"},
    {"q": "Who is the Commander in Chief of the military?", "a": "The President"},
    {"q": "What is Independence Day?", "a": "The country's birthday"},
    {"q": "What is Memorial Day?", "a": "A holiday to honor soldiers who died in military service"},
    {"q": "What is Veterans Day?", "a": "A holiday to honor people in the U.S. military"}
    # Comrade, add the rest of your 128 questions here!
]

class SovereignQuizzer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sovereign Civics Master 2026")
        self.root.geometry("600x500")
        self.root.configure(bg="#1a1a1a")

        # MISSION TRACKERS
        self.questions = list(quiz_data)
        random.shuffle(self.questions)
        self.current_index = 0
        self.score = 0
        self.wrong_count = 0  # Tracking failures for the 9-wrong rule

        # UI SETUP
        self.setup_ui()
        self.load_question()

    def setup_ui(self):
        self.title_label = tk.Label(
            self.root, text="N-400 MISSION CONTROL", 
            font=("Courier", 22, "bold"), fg="#00ff00", bg="#1a1a1a"
        )
        self.title_label.pack(pady=30)

        self.question_label = tk.Label(
            self.root, text="", font=("Verdana", 14), 
            fg="white", bg="#1a1a1a", wraplength=500, justify="center"
        )
        self.question_label.pack(pady=10)

        self.entry = tk.Entry(
            self.root, font=("Consolas", 18), 
            justify="center", bg="#333", fg="white", insertbackground="white"
        )
        self.entry.pack(pady=20)
        self.entry.bind('<Return>', lambda e: self.check_answer())
        self.entry.focus_set() 

        self.submit_btn = tk.Button(
            self.root, text="VALIDATE LOGIC", command=self.check_answer, 
            font=("Arial", 12, "bold"), bg="#27ae60", fg="white", 
            width=20, cursor="hand2"
        )
        self.submit_btn.pack(pady=10)

        self.status_label = tk.Label(
            self.root, text="", font=("Courier", 10), 
            fg="#888", bg="#1a1a1a"
        )
        self.status_label.pack(side="bottom", pady=20)

    def load_question(self):
        if self.current_index < len(self.questions):
            q_text = self.questions[self.current_index]["q"]
            self.question_label.config(text=f"ANALYZING TARGET {self.current_index + 1}:\n\n{q_text}")
            self.entry.delete(0, tk.END)
            self.update_status()
        else:
            # If we run out of questions before hitting 12 or 9
            messagebox.showinfo("Mission End", "No more questions in the cargo bay.")
            self.root.destroy()

    def update_status(self):
        lives_left = 9 - self.wrong_count
        status_text = f"SCORE: {self.score}/12 | LIVES: {lives_left} | PROGRESS: {self.current_index + 1}"
        self.status_label.config(text=status_text)

    def check_answer(self):
        user_ans = self.entry.get().strip().lower()
        correct_ans = self.questions[self.current_index]["a"].lower()

        # LOGIC INSPECTION
        # Matches if the answer is exact OR if the user's long answer contains the keyword
        if user_ans == correct_ans or (len(user_ans) > 3 and user_ans in correct_ans):
            self.score += 1
            messagebox.showinfo("SUCCESS", "Variable Verified. Correct!")
        else:
            self.wrong_count += 1
            messagebox.showerror("GLITCH", f"Incorrect.\nSystem requires: {self.questions[self.current_index]['a']}")

        # THRESHOLD CHECKS
        if self.score >= 12:
            messagebox.showinfo("MISSION SUCCESS", "PROMOTED: 12 Correct. You passed the inspection!")
            self.root.destroy()
            return

        if self.wrong_count >= 9:
            messagebox.showwarning("MISSION FAILURE", "CRITICAL ERROR: 9 Failures Detected.\nSystem Lockdown.")
            self.root.destroy()
            return

        # NEXT TARGET
        self.current_index += 1
        self.load_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = SovereignQuizzer(root)
    root.mainloop()