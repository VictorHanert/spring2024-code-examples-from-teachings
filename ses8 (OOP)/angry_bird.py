import random

class Bird:
    def __init__(self, x=0, y=0, direction='right'):
        self.x = x
        self.y = y
        self.direction = direction
    
    def move_forward(self):
        if self.direction == 'right':
            self.x += 1
        elif self.direction == 'left':
            self.x -= 1
        elif self.direction == 'up':
            self.y -= 1
        elif self.direction == 'down':
            self.y += 1
    
    def turn_left(self):
        if self.direction == 'right':
            self.direction = 'up'
        elif self.direction == 'up':
            self.direction = 'left'
        elif self.direction == 'left':
            self.direction = 'down'
        elif self.direction == 'down':
            self.direction = 'right'
    
    def turn_right(self):
        if self.direction == 'right':
            self.direction = 'down'
        elif self.direction == 'down':
            self.direction = 'left'
        elif self.direction == 'left':
            self.direction = 'up'
        elif self.direction == 'up':
            self.direction = 'right'
    
    def win_action(self):
        print("""--------------------------------------
Congratulations! You hit the pig! Press 'a' to try again!
-----------------------------------------""")


class Pig:
    def __init__(self, board_size):
        self.x = random.randint(0, board_size - 1)
        self.y = random.randint(0, board_size - 1)

class Board:
    def __init__(self, board_size):
        self.board_size = board_size
        self.bird = Bird()
        self.pig = Pig(board_size)
    
    def display(self):
        for y in range(self.board_size):
            for x in range(self.board_size):
                if x == self.bird.x and y == self.bird.y:
                    print('B', end=' ')
                elif x == self.pig.x and y == self.pig.y:
                    print('P', end=' ')
                else:
                    print('*', end=' ')
            print()

    def run(self):
        self.display()
        while True:
            command = input("Enter command (f: forward, l: turn left, r: turn right, q: quit): ")
            if command == 'f':
                self.bird.move_forward()
            elif command == 'l':
                self.bird.turn_left()
            elif command == 'r':
                self.bird.turn_right()
            elif command == 'q':
                break
            else:
                print("Invalid command!")
            
            # Check if bird hits the pig
            if self.bird.x == self.pig.x and self.bird.y == self.pig.y:
                self.bird.win_action()
                break
            
            self.display()


class Workspace:
    def display(self):
        print("Welcome to Angry Birds!")
        print("Instructions:")
        print("  - Enter 'f' to move the bird forward.")
        print("  - Enter 'l' to turn the bird left.")
        print("  - Enter 'r' to turn the bird right.")
        print("  - Enter 'q' to quit the game.")

    def get_commands(self):
        commands = []
        while True:
            command = input("Enter command (f: forward, l: turn left, r: turn right, q: quit): ")
            if command == 'q':
                break
            commands.append(command)
        return commands


class Game:
    def __init__(self):
        self.workspace = Workspace()

    def run(self):
        self.workspace.display()
        board_size = int(input("Choose a board-size for the game. (10 is recommended):  "))
        board = Board(board_size)
        board.run()


if __name__ == "__main__":
    game = Game()
    game.run()

game.run()