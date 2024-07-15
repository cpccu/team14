class Quiz:
    def __init__(self):
        self.questions = [
            {
                "question": "What is the capital of Bangladesh?",
                "options": ["1. Dhaka", "2. Chittagong", "3. Khulna", "4. Rajshahi"],
                "answer": 1
            },
            {
                "question": "Which river is known as the lifeline of Bangladesh?",
                "options": ["1. Padma", "2. Jamuna", "3. Meghna", "4. Brahmaputra"],
                "answer": 1
            },
            {
                "question": "What is the national flower of Bangladesh?",
                "options": ["1. Rose", "2. Water Lily", "3. Marigold", "4. Lotus"],
                "answer": 2
            },
            {
                "question": "When did Bangladesh gain independence?",
                "options": ["1. 1947", "2. 1952", "3. 1971", "4. 1981"],
                "answer": 3
            },
            {
                "question": "Who is known as the Father of the Nation in Bangladesh?",
                "options": ["1. Sheikh Hasina", "2. Ziaur Rahman", "3. Sheikh Mujibur Rahman", "4. Hossain Muhammad Ershad"],
                "answer": 3
            }
        ]
        self.score = 0

    def ask_question(self, question_data):
        print("\n" + question_data["question"])
        for option in question_data["options"]:
            print(option)
        user_answer = int(input("Enter the number of your answer: "))
        if user_answer == question_data["answer"]:
            return True
        else:
            correct_option = question_data["options"][question_data["answer"] - 1]
            print(f"Wrong.\nThe correct answer is: {correct_option.split('. ', 1)[1]}")
            return False

    def start_quiz(self):
        for question_data in self.questions:
            if self.ask_question(question_data):
                print("Correct!")
                self.score += 1
            
        self.display_score()

    def display_score(self):
        print("\n============================")
        print(f"Your final score is: {self.score}/{len(self.questions)}")
        print("============================\n")

if __name__ == "__main__":
    quiz = Quiz()
    quiz.start_quiz()
