class Questions:
    def __init__(self,prompt,answer):
        self.prompt = prompt
        self.answer = answer
        self.question = []
class Quiz:
    def __init__(self):
        self.question = []
    def add_question(self,prompt, answer):
        quest = Questions(prompt,answer)
        self.question.append(quest)
        self.save_questions()
    def take_quiz(self):
        score = 0
        for q in self.question:
            print(f'question,{q.prompt}')
            user_ans = input("Answer: ")
            if user_ans.lower() == q.answer.lower():
                print('Correct!')
                score +=1
            else:
                print('Wrong')
        print(f'Final Score:{score}')
        self.save_score(score)
    def save_questions(self):
        with open('Quiz.txt','w') as f:
            for Quiz in self.question:
                f.write(f'{Quiz.prompt} ,{Quiz.answer}\n')

    def load_questions(self):
        try:
            with open('Quiz.txt','r') as f:
                for line in f:
                    line = line.strip()
                    question,answer = line.split(',')
                    loaded= Questions(question,answer)
                    self.question.append(loaded)
        except FileNotFoundError:
            print('FIle Not Found!!')
    def save_score(self, score):
        with open('leaderboard.txt','a') as f:
            f.write(f'score: {score}\n')


game = Quiz()
game.add_question("What is 2+2?", "4")
game.add_question("Capital of France?", "Paris")

# This starts the interactive game!
game.take_quiz()




