from game.scripting.action import Action

class Grow (Action):

    def execute (self, cast, script):
        """Snake grows. Make it execute less times. It is growing exponentially right now. 
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score = cast.get_first_actor("scores")
        # score = cast.get_second_actor("scores") pending add to main
        snake = cast.get_first_actor("snakes")
        snake_2 = cast.get_first_actor("snakes")
        head = snake.get_head()

        snake.grow_tail (1)
        snake_2.grow_tail (1)

        # if head.get_position().equals(food.get_position()):
        #     snake.grow_tail(points)
        #     score.add_points(points)
        #     food.reset()