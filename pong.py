# Steven Lessard
# Pong module
# Comp50GD - Lab4

""" This module features a pong game designed for two players """

import pygame, sys
from pygame.locals import *

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
PADDLE1_START_X = 10
PADDLE2_START_X = SCREEN_WIDTH - 20
PADDLE_START_Y = 20
DIV_WIDTH = 5
DIV_HEIGHT = SCREEN_HEIGHT
DIV_START_X = SCREEN_WIDTH/2 - DIV_WIDTH/2
DIV_START_Y = 0
BALL_SPEED = 10
BALL_WIDTH_HEIGHT = 16
POINTS_TO_WIN = 11

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

def load_sound(sound_name):
    try:
        sound = pygame.mixer.Sound(sound_name)
    except pygame.error, message:
        print "Cannot load sound: " + sound_name
        raise SystemExit, message
    return sound

# Collision sound
collideSound = load_sound('laser.wav')

# This is a rect that contains the ball at the beginning it is set in the center of the screen
ball_rect = pygame.Rect((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), (BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT))

# Speed of the ball (x, y)
ball_speed = [BALL_SPEED, BALL_SPEED]

# P1 paddle vertically centered on the left side
paddle1_rect = pygame.Rect((PADDLE1_START_X, PADDLE_START_Y), (PADDLE_WIDTH, PADDLE_HEIGHT))

# P2 paddle vertically centered on the right side
paddle2_rect = pygame.Rect((PADDLE2_START_X, PADDLE_START_Y), (PADDLE_WIDTH, PADDLE_HEIGHT))

# Screen Divider
div_rect = pygame.Rect((DIV_START_X, DIV_START_Y), (DIV_WIDTH, DIV_HEIGHT))

# Scoring: 1 point if you hit the ball, -5 point if you miss the ball
p1Score = 0 # Paddle on the left side of the screen
p2Score = 0 # Paddle on the right side of the screen

# Load the font for displaying the scores
font = pygame.font.Font(None, 30)
fontWin = pygame.font.Font(None, 36)

# Game loop
while True:
    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
            pygame.quit()
        # Control the paddle with the mouse
        elif event.type == pygame.MOUSEMOTION:
            paddle1_rect.centery = event.pos[1]
            # correct paddles' positions if they're going out of window
            if paddle1_rect.top < 0:
                paddle1_rect.top = 0
            elif paddle1_rect.bottom >= SCREEN_HEIGHT:
                paddle1_rect.bottom = SCREEN_HEIGHT
            if paddle2_rect.top < 0:
                paddle2_rect.top = 0
            elif paddle2_rect.bottom >= SCREEN_HEIGHT:
                paddle2_rect.bottom = SCREEN_HEIGHT

    # P1 Controls
    if pygame.key.get_pressed()[pygame.K_w] and paddle1_rect.top > 0:
        paddle1_rect.top -= BALL_SPEED
    elif pygame.key.get_pressed()[pygame.K_s] and paddle1_rect.bottom < SCREEN_HEIGHT:
        paddle1_rect.top += BALL_SPEED

    # P2 Controls
    if pygame.key.get_pressed()[pygame.K_UP] and paddle2_rect.top > 0:
        paddle2_rect.top -= BALL_SPEED
    elif pygame.key.get_pressed()[pygame.K_DOWN] and paddle2_rect.bottom < SCREEN_HEIGHT:
        paddle2_rect.top += BALL_SPEED

    # Quit Button    
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        sys.exit(0)
        pygame.quit()
        
    # Update ball position
    ball_rect.left += ball_speed[0]
    ball_rect.top += ball_speed[1]

    # Ball collision with rails
    if ball_rect.top <= 0 or ball_rect.bottom >= SCREEN_HEIGHT:
        ball_speed[1] = -ball_speed[1]
    if ball_rect.right >= SCREEN_WIDTH: # Player 2 scores
        ball_speed[0] = -ball_speed[0]
        p2Score += 1
    if ball_rect.left <= 0:             # Player 1 scores
        ball_speed[0] = -ball_speed[0]
        p1Score += 1

    if p1Score > (POINTS_TO_WIN - 1) or p2Score > (POINTS_TO_WIN - 1) : # Winning conditions
        cont = True
        while cont: # Game over state
            if p1Score > (POINTS_TO_WIN - 1):
                winText = fontWin.render("P1 wins, enter to play again", True, (0, 255, 0))
            else:
                winText = fontWin.render("P2 wins, enter to play again", True, (255, 0, 0))
    
            screen.fill((0, 0, 0))
            screen.blit(winText, (50, 50))

            # Quit Button    
            for event in pygame.event.get():
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit(0)
                elif event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit() 
                elif event.key == K_RETURN:
                    cont = False
                    p1Score = 0
                    p2Score = 0
            pygame.display.flip()

    # Test if the ball is hit by the paddle; if yes reverse speed and add a point
    if paddle1_rect.colliderect(ball_rect) or paddle2_rect.colliderect(ball_rect):
        ball_speed[0] = -ball_speed[0]
        collideSound.play()
    
    # Clear screen
    screen.fill((255, 255, 255))

    # Draw the middle divide of the game screen
    pygame.draw.rect(screen, (255, 0, 0), div_rect)

    # Render the ball, the paddle, and the score
    pygame.draw.rect(screen, (0, 0, 0), paddle1_rect) # P1 paddle
    pygame.draw.rect(screen, (0, 0, 0), paddle2_rect) # P2 paddle
    pygame.draw.circle(screen, (0, 0, 0), ball_rect.center, ball_rect.width / 2) # The ball

    score_text1 = font.render("P1: "+str(p1Score), True, (0, 0, 0))
    score_text2 = font.render("P2: "+str(p2Score), True, (0, 0, 0))
    screen.blit(score_text1, ((SCREEN_WIDTH / 4) - font.size(str(p1Score))[0] / 2, 5)) # The score for player 1
    screen.blit(score_text2, ((3 * (SCREEN_WIDTH / 4)) - font.size(str(p2Score))[0] / 2, 5)) # The score for player 2

    # Update screen and wait 20 milliseconds
    pygame.display.flip()
    pygame.time.delay(20)

