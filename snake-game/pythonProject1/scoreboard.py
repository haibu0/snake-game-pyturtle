from turtle import Turtle

STARTING_SCORE = 0
STARTING_POSITION_SCOREBOARD = (0,250)
ALIGNMENT = "center"
FONT = ("Arial", 20, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(STARTING_POSITION_SCOREBOARD)
        self.score = STARTING_SCORE
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)
