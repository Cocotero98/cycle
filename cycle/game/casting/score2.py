from turtle import pos
from game.casting.score import Score
from game.shared.point import Point
from game.casting.actor import Actor

# class Score2(Score):
#     def __init__(self):
#         super().__init__()
#         position=Point(400, 15)
#         self.set_position(position)

#     def set_position(self, position):
        
#         Actor().set_position(position)

#     def add_points(self, points):
#         return super().add_points(points)

class Score2(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        self._position = Point(780, 0)
        self._points = 0
        self.add_points(0)

    # def set_position(self, position):
        
    #     Actor().set_position(position)

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"Player Two: {self._points}")