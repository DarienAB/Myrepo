from turtle import Turtle

# Constants for initial snake setup
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Positions of the snake's initial 3 segments
MOVE_DISTANCE = 20  # Distance the snake moves forward each time
UP = 90  # Angle for the snake to move up (90 degrees)
DOWN = 270  # Angle for the snake to move down (270 degrees)
LEFT = 180  # Angle for the snake to move left (180 degrees)
RIGHT = 0  # Angle for the snake to move right (0 degrees)

class Snake:
    def __init__(self):
        self.segments = []  # List to hold all the segments (parts) of the snake
        self.create_snake()  # Method to create the initial snake body
        self.head = self.segments[0]  # The first segment is the snake's head

    def create_snake(self):
        # Create the snake by adding segments at the starting positions
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
            new_segment = Turtle("square")  # Create a new turtle shape "square" to represent a segment
            new_segment.color("white")  # Set the color of each segment to white
            new_segment.penup()  # Prevents the segment from drawing lines on the screen
            new_segment.goto(position)  # Move the segment to its starting position
            self.segments.append(new_segment)  # Add the segment to the list of segments
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]  # The first segment is the snake's head
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        # Move the snake by shifting each segment to the position of the segment in front of it
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()  # Get the x-coordinate of the previous segment
            new_y = self.segments[seg_num - 1].ycor()  # Get the y-coordinate of the previous segment
            self.segments[seg_num].goto(new_x, new_y)  # Move the current segment to the position of the previous one

        # Move the head of the snake forward
        self.segments[0].forward(MOVE_DISTANCE)  # Move the head segment 20 units forward

    # Method to turn the snake up, but only if it's not moving down
    def up(self):
        if self.head.heading() != DOWN:  # Prevents the snake from moving in the opposite direction (down)
            self.head.setheading(UP)  # Set the head's direction to up (90 degrees)

    # Method to turn the snake down, but only if it's not moving up
    def down(self):
        if self.head.heading() != UP:  # Prevents the snake from moving in the opposite direction (up)
            self.head.setheading(DOWN)  # Set the head's direction to down (270 degrees)

    # Method to turn the snake left, but only if it's not moving right
    def left(self):
        if self.head.heading() != RIGHT:  # Prevents the snake from moving in the opposite direction (right)
            self.head.setheading(LEFT)  # Set the head's direction to left (180 degrees)

    # Method to turn the snake right, but only if it's not moving left
    def right(self):
        if self.head.heading() != LEFT:  # Prevents the snake from moving in the opposite direction (left)
            self.head.setheading(RIGHT)  # Set the head's direction to right (0 degrees)
