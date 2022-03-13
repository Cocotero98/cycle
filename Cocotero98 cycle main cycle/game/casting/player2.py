import constants
from game.casting.actor import Actor
from game.casting.snake import Snake
from game.shared.point import Point

class Player2(Snake):
    def __init__(self):
        """calls the '__init__()' method of the super class (Snake)"""
        super().__init__()
    def get_segments(self):
        """gets the segments of the snake"""
        return self._segments

    def move_next(self):
        """calls the 'move_next()' method of the super class (Snake)"""
        super().move_next()

    def get_head(self):
        """determines which index will be the head of the snake"""
        return self._segments[0]

    def grow_tail(self, number_of_segments, color):
        """calls the 'grow_tail()' method of the super class (Snake)"""
        super().grow_tail(number_of_segments, color)

    def turn_head(self, velocity):
        """moves the head towards the input direction at the set speed"""
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        """builds the snake's body for the game to start"""
        x = int(constants.MAX_X / 2)+int(constants.MAX_X / 4)
        y = int(constants.MAX_Y / 2)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = constants.YELLOW if i == 0 else constants.BLUE
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)
    def clear_segments(self):
        """calls the 'clear_segments()' method of the super class (Snake)"""
        return super().clear_segments()