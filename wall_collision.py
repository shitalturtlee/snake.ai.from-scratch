def hits_wall(head):
    x, y = head
    return x < 0 or x >= GRID_WIDTH or y < 0 or y >= GRID_HEIGHT
def hits_self(snake):
    head = snake[0]
    return head in snake[1:]
OPPOSITES = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}

def is_valid_turn(current_direction, new_direction):
    return new_direction != OPPOSITES[current_direction]
if __name__ == "__main__":
    snake = [(5, 5), (4, 5), (3, 5)]
    direction = "RIGHT"
    food = spawn_food(snake)

    for step in range(8):
        snake = move_snake(snake, direction, ate_food=False)
        print(f"Step {step + 1}")
        print_grid(snake, food)   # note: this will fail once head leaves the grid, see below

        if hits_wall(snake[0]):
            print("Hit a wall! Game over.")
            break
        if hits_self(snake):
            print("Hit itself! Game over.")
            break
