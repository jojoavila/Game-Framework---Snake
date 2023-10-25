import pygame  # Import the Pygame library for game development.
import time
import random
import pygame.mixer # module to play a sound

pygame.init()  # Initialize the Pygame library.

# Define color constants for later use in the game.
white = (255, 255, 255)
yellow = (254, 239, 222)
black = (167, 161, 174)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (55, 93, 138)

# Set the dimensions of the game window.
dis_width = 600
dis_height = 400

# Create the game window using Pygame.
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')  # Set the title of the game window.

clock = pygame.time.Clock()  # Create a clock object to control the game's frame rate.

snake_block = 10  # Define the size of the snake blocks.
snake_speed = 15  # Define the initial speed of the snake.

# Define fonts for displaying text in the game.
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("arial", 35)


# Define a function to display the player's score.
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


# Define a function to draw the snake on the game window.
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


# Define a function to display a message on the game window.
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


# Define the main game loop.
def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []  # Initialize an empty list to store the snake's coordinates.
    Length_of_snake = 1  # Initialize the length of the snake.

    # Generate initial coordinates for the food that the snake will eat.
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    #Initialize the mixer and load a sound file 
    pygame.mixer.init() 
    eat_sound = pygame.mixer.Sound("eat.wav")

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()  # Restart the game when 'C' key is pressed.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                # Respond to arrow key inputs to change the snake's direction.
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Check if the snake hits the game boundaries. If so, end the game.
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        dis.fill(blue)  # Fill the game window with a blue background.
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])  # Draw the food.

        snake_Head = []  # Create a list to store the snake's head coordinates.
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)  # Add the head coordinates to the snake's list.

        if len(snake_List) > Length_of_snake:
            del snake_List[0]  # Remove the tail of the snake to maintain its length.

        # Check if the snake collides with itself. If so, end the game.
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Draw the snake on the game window.
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)  # Display the player's score.

        pygame.display.update()  # Update the game window.

        # Check if the snake has eaten the food and increase the snake's length.
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            eat_sound.play()  # Play the sound when the snake eats the food

        clock.tick(snake_speed)  # Control the game's frame rate.

    pygame.quit()  # Quit Pygame.
    quit()


gameLoop()  # Start the game loop.