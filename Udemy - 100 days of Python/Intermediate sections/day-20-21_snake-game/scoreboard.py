from turtle import Turtle
from settings import SCREEN_HEIGHT

# Scoreboard settings
TEXT_ALIGN = "center"
FONT_SIZE = 15
FONT = ("Courier", FONT_SIZE, "bold")

class Scoreboard(Turtle):
    """Models the scoreboard in the Snake Game. It inherities from the Turtle class"""
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        # keeps track of the score -> starts at 0
        self.score = 0
        # keeps track of the high score -> starts at 0
        self.high_score = 0
        # sets the location of the text in the screen
        self.goto(0, (SCREEN_HEIGHT / 2) - FONT_SIZE * 2)
        self.render_score()
    
    def render_score(self):
        """Renders score text on the screen"""
        self.clear()
        self.write(f"Score: {self.score}  |  High Score: {self.high_score}", align=TEXT_ALIGN, font=FONT)

    def increase_score(self):
        """Increases score by one and updates the rendered text"""
        self.score += 1
        self.render_score()

    # def game_over(self):
    #     """Renders game over text at the center of the screen"""
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align=TEXT_ALIGN, font=FONT)

    def reset_score(self):
        """Replaces high score if it was beaten, and resets score for a new game"""
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.render_score()
        
