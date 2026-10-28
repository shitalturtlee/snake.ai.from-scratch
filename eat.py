def next_head(snake, direction):
    head_x, head_y = snake[0]
    dx, dy = DIRECTIONS[direction]
    return (head_x + dx, head_y + dy)
def step(snake, direction, food, score):
    new_head = next_head(snake, direction)
    ate_food = (new_head == food)

    snake = move_snake(snake, direction, ate_food)

    if ate_food:
        score += 1
        food = spawn_food(snake)   # new food, avoiding the (now longer) snake

    game_over = hits_wall(snake[0]) or hits_self(snake)

    return snake, food, score, game_over
def reset_game():
    snake = [(5, 5), (4, 5), (3, 5)]
    direction = "RIGHT"
    food = spawn_food(snake)
    score = 0
    return snake, direction, food, score
if __name__ == "__main__":
    snake, direction, food, score = reset_game()

    # Hardcoded moves for testing: head toward the food manually
    moves = ["RIGHT", "RIGHT", "DOWN", "DOWN", "LEFT", "LEFT", "UP"]

    for m in moves:
        if not is_valid_turn(direction, m):
            continue
        direction = m
        snake, food, score, game_over = step(snake, direction, food, score)

        print(f"Move: {m} | Score: {score}")
        if game_over:
            print("Game over!")
            break
        print_grid(snake, food)
