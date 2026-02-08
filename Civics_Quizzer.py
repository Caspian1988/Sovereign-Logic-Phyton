import random

# 1. The "Sovereign Database" (Questions & Answers)
# We use a Dictionary { "Question": "Answer" }
questions = {
    "What is the supreme law of the land?": "the Constitution",
    "What does the Constitution do?": "sets up the government",
    "The idea of self-government is in the first three words of the Constitution. What are these words?": "We the People",
    "What is an amendment?": "a change to the Constitution",
    "What do we call the first ten amendments to the Constitution?": "the Bill of Rights"
}

def run_quiz():
    score = 0
    question_list = list(questions.keys())
    
    print("--- CASPIAN1988 CIVICS COMMAND CENTER ---")
    print("Type 'exit' to stop the simulation.\n")

    while True:
        # Pick a random variable from the database
        current_q = random.choice(question_list)
        correct_a = questions[current_q]

        # Get User Input
        user_answer = input(f"QUESTION: {current_q}\nYOUR ANSWER: ").lower()

        if user_answer == 'exit':
            print(f"\nSimulation Terminated. Final Score: {score}")
            break

        # Check Logic (Detailed Inspection)
        if user_answer in correct_a.lower():
            print(">>> STATUS: CORRECT. Logic verified.\n")
            score += 1
        else:
            print(f">>> STATUS: ERROR. Correct Answer: {correct_a}\n")

# Execute the Script
if __name__ == "__main__":
    run_quiz()