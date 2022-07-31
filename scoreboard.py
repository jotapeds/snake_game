from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')
with open("data.txt", mode ='r') as f:
    HS = int(f.read())

class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = HS
        self.color('white')
        self.pu()
        self.goto(0,265)
        self.hideturtle()
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT,font=FONT)
        
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode ='w') as f:
                f.write(str(self.high_score))
            

        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write('GAME OVER',align= ALIGNMENT,font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()