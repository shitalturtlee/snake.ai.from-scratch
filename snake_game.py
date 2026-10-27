import random

GRID_WIDTH = 10
GRID_HEIGHT = 10

# Each element is an (x, y) tuple. First element = head.
snake = [(5, 5), (4, 5), (3, 5)]   # starts 3 segments long, moving right

direction = "RIGHT"   # current direction: UP, DOWN, LEFT, RIGHT

def spawn_food(snake):
    while True:
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if food not in snake:   # don't spawn food inside the snake's body
            return food

food = spawn_food(snake)
DIRECTIONS = {
    "UP":    (0, -1),
    "DOWN":  (0, 1),
    "LEFT":  (-1, 0),
    "RIGHT": (1, 0),
}

def move_snake(snake, direction):
    head_x, head_y = snake[0]
    dx, dy = DIRECTIONS[direction]
    new_head = (head_x + dx, head_y + dy)

    new_snake = [new_head] + snake[:-1]   # add new head, drop the tail
    return new_snake
def print_grid(snake, food):
    for y in range(GRID_HEIGHT):
        row = ""
        for x in range(GRID_WIDTH):
            if (x, y) == snake[0]:
                row += "H"   # head
            elif (x, y) in snake:
                row += "o"   # body
            elif (x, y) == food:
                row += "F"   # food
            else:
                row += "."
        print(row)
    print()

snake = [(5, 5), (4, 5), (3, 5)]
direction = "RIGHT"
food = spawn_food(snake)

print_grid(snake, food)
snake = move_snake(snake, direction, ate_food=False)
print_grid(snake, food)

