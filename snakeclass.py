from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        # super().__init__(Turtle)
        self.turtle_list = []
        self.create_snake()
        self.head = self.turtle_list[0]

    def create_snake(self):
        for i in POSITIONS:
            self.add_turtle(i)

    def add_turtle(self, i):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(i)
        self.turtle_list.append(segment)

    def reset(self):
        for seg in self.turtle_list:
            seg.goto(1000, 1000)
        self.turtle_list.clear()
        self.create_snake()
        self.head = self.turtle_list[0]

    def extend(self):
        self.add_turtle(self.turtle_list[-1].position())

    def move(self):
        for i in range(len(self.turtle_list) - 1, 0, -1):
            new_x = self.turtle_list[i - 1].xcor()
            new_y = self.turtle_list[i - 1].ycor()
            self.turtle_list[i].goto(new_x, new_y)
        self.turtle_list[0].forward(MOVE_DISTANCE)

    def up(self):
        tim = self.turtle_list[0]
        if tim.heading() != DOWN:
            tim.setheading(UP)
        else:
            pass


    def down(self):
        tim = self.turtle_list[0]
        if tim.heading() != UP:
            tim.setheading(DOWN)
        else:
            pass

    def left(self):
        tim = self.turtle_list[0]
        if tim.heading() != RIGHT:
            tim.setheading(LEFT)
        else:
            pass

    def right(self):
        tim = self.turtle_list[0]
        if tim.heading() != LEFT:
            tim.setheading(RIGHT)
        else:
            pass
