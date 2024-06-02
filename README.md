# Classical-Snake-Game-Python
The Snake Game project is a classic snake game implemented using the Turtle graphics module in Python. The project showcases object-oriented programming (OOP) principles and interactive game design, providing an engaging experience for users.

# Snake Game Project Description

## Overview
The Snake Game project is a classic snake game implemented using the Turtle graphics module in Python. This project comprises four main components, each housed in a separate Python file: the main game logic (`main.py`), the snake class (`snakeclass.py`), the food class (`food.py`), and the scoreboard class (`scoreboard.py`). The project showcases object-oriented programming (OOP) principles and interactive game design, providing an engaging experience for users.

## Features
- **Classic Snake Gameplay:** Move the snake to eat food, grow longer, and avoid collisions with the walls and itself.
- **High Score Tracking:** Keeps track of the highest score achieved during the game.
- **Interactive Controls:** Use the arrow keys to control the snake's direction.
- **Dynamic Game Elements:** Randomly positioned food and a continuously updating score display.
- **Responsive Design:** Smooth animation and real-time interaction with user inputs.

## User-Defined Classes and Functions

### Main Game Logic (`main.py`)
#### User-Defined Functions
- **Game Loop**
  - Initializes the game components (snake, food, scoreboard).
  - Sets up key bindings for snake movement.
  - Runs the main game loop, updating the screen, moving the snake, and checking for collisions.


### Snake Class (`snakeclass.py`)
#### User-Defined Methods
- **`__init__()`**
  - Initializes the snake object with a list of segments.
- **`create_snake()`**
  - Creates the initial snake with three segments.
- **`add_turtle(position)`**
  - Adds a new segment to the snake at the specified position.
- **`reset()`**
  - Resets the snake to its initial state.
- **`extend()`**
  - Adds a new segment to the snake, making it longer.
- **`move()`**
  - Moves the snake forward by updating the position of each segment.
- **`up()`**
  - Changes the snake's direction to up if it's not currently moving down.
- **`down()`**
  - Changes the snake's direction to down if it's not currently moving up.
- **`left()`**
  - Changes the snake's direction to left if it's not currently moving right.
- **`right()`**
  - Changes the snake's direction to right if it's not currently moving left.

### Food Class (`food.py`)
#### User-Defined Methods
- **`__init__()`**
  - Initializes the food object, sets its shape, color, and position.
- **`relocate()`**
  - Randomly positions the food on the screen.

### Scoreboard Class (`scoreboard.py`)
#### User-Defined Methods
- **`__init__()`**
  - Initializes the scoreboard, reads the high score from a file, and displays the welcome message.
- **`increment_score()`**
  - Increases the score by one and updates the display.
- **`show_score()`**
  - Displays the current score and high score on the screen.
- **`reset_game()`**
  - Resets the game score and updates the high score if a new high score is achieved.


### Turtle Module Functions/Methods:
1. `turtle.Screen()`: Creates a screen object for the game.
2. `screen.setup(width, height)`: Configures the screen size.
3. `screen.bgcolor(color)`: Sets the background color of the screen.
4. `screen.title(title)`: Sets the title of the game window.
5. `screen.tracer(0)`: Disables automatic screen updates for smoother animation.
6. `screen.update()`: Manually updates the screen to display changes.
7. `screen.listen()`: Sets the screen to listen for key events.
8. `screen.onkey(fun, key)`: Binds a function to a specific key press event.
9. `screen.exitonclick()`: Keeps the screen open until a mouse click event occurs.
10. `time.sleep(seconds)`: Delays the execution of the program for the specified duration.
11. `turtle.Turtle()`: Creates a new turtle object for drawing.
12. `turtle.Turtle().shape(shape)`: Sets the shape of the turtle.
13. `turtle.Turtle().color(color)`: Sets the color of the turtle.
14. `turtle.Turtle().penup()`: Lifts the pen to move without drawing.
15. `turtle.Turtle().goto(x, y)`: Moves the turtle to the specified coordinates.
16. `turtle.Turtle().forward(distance)`: Moves the turtle forward by the specified distance.
17. `turtle.Turtle().heading()`: Returns the current heading of the turtle.
18. `turtle.Turtle().setheading(angle)`: Sets the heading of the turtle to the specified angle.
19. `turtle.Turtle().clear()`: Clears the turtle's drawings on the screen.
20. `turtle.Turtle().hideturtle()`: Hides the turtle cursor.
21. `turtle.Turtle().write(arg, align, font)`: Writes text on the screen.
22. `turtle.Turtle().shapesize(stretch_wid, stretch_len)`: Stretches the turtle's shape.
23. `turtle.Turtle().speed(speed)`: Sets the drawing speed of the turtle.

### Python Built-in Functions/Methods:
1. `super().__init__()`: Calls the constructor of the superclass.
2. `open(filename, mode)`: Opens a file with the specified name and mode.
3. `file.read()`: Reads and returns the contents of the file.
4. `file.write(data)`: Writes data to the file.

## Future Enhancements
- **Enhanced Graphics:** Improve the visual design of the game with better graphics and animations.
- **Sound Effects:** Add sound effects for different game events, such as eating food and collisions.
- **Difficulty Levels:** Introduce different difficulty levels with varying speeds and obstacles.
- **Multiplayer Mode:** Implement a multiplayer mode where two players can control separate snakes on the same screen.

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue if you have suggestions for improvements or encounter any bugs.
