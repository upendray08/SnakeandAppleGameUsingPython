# Snake Game

This is a classic Snake game implemented in Python using the `pygame` library. The game involves controlling a snake and eating apples to grow longer. The objective is to achieve the highest possible score without colliding with the snake's own body or the game boundaries.

## Requirements:
- Python 3
- Pygame library

## How to Play:
1. Run the script, and the game window will appear.
2. Control the snake's direction using the arrow keys (up, down, left, right).
3. Move the snake to eat the green apples that randomly appear on the screen.
4. Each apple eaten will increase the snake's length by one block.
5. The game will end if the snake collides with its own body or the game boundaries.
6. After the game ends, you can restart the game by pressing the "Enter" key.
7. To exit the game, press the "Esc" key or close the game window.

## Game Mechanics:
- The snake starts with a length of one block and moves in the "right" direction.
- It can change direction by pressing the arrow keys accordingly.
- The snake's movement is continuous, and it grows longer by one block whenever it eats an apple.
- If the snake's head collides with its own body or goes beyond the game boundaries, the game ends.
- The game will display the player's score (the length of the snake - 1) at the top-right corner of the screen.
- The speed of the snake will increase after the score exceeds 10.

## Controls:
- Arrow Up: Move the snake up
- Arrow Down: Move the snake down
- Arrow Left: Move the snake left
- Arrow Right: Move the snake right
- Enter: Restart the game (after game over)
- Esc: Exit the game

## Game Objects:
- Snake: Controlled by the player, it grows longer by eating apples.
- Apple: Green blocks that appear randomly on the screen for the snake to eat.

## Scoring:
- The player's score is calculated based on the length of the snake. Each apple eaten increases the score by one point.

Enjoy playing the Snake Game! Try to beat your high score and have fun!
