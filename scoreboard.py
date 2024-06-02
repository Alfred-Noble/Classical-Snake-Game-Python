from turtle import Turtle
FONT_MAIN = ("Arial", 22, "italic")
FONT = ("Arial", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(-20, 260)
        self.color("white")
        self.write(f"Welcome to the Snake Game", align="center", font=FONT_MAIN)

    def increment_score(self):
        self.score += 1
        self.show_score()

    def show_score(self):
        self.goto(-10, 270)
        self.clear()
        self.color("white")
        self.write(f"Score: {self.score} High Score: {self.high_score} ", align="center", font=FONT)

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.show_score()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align="center", font=FONT_MAIN)
