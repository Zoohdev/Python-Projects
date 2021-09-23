import pygame
import random

pygame.init()

screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width, screen_height))

player = pygame.image.load("image.png")
enemy1 = pygame.image.load("enemy.png")
enemy2 = pygame.image.load("monster.png")
enemy3 = pygame.image.load("satan.png")

image_height = player.get_height()
image_width = player.get_width()
enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()

print("This is the height of the player image: " + str(image_height))
print("This is the width of the player image: " + str(image_width))
print("This is the height of the first enemy image: " + str(enemy1_height))
print("This is the width of the first enemy image: " + str(enemy1_width))
print("This is the height of the second enemy image: " + str(enemy2_height))
print("This is the width of the second enemy image: " + str(enemy2_width))
print("This is the height of the third enemy image: " + str(enemy3_height))
print("This is the width of the third enemy image: " + str(enemy3_width))

playerXPosition = 100
playerYPosition = 50

enemy1XPosition = screen_width
enemy1YPosition = random.randint(0, screen_height - enemy_height)

enemy2XPosition = screen_width
enemy2YPosition = random.randint(0, screen_height - enemy_height)

enemy3XPosition = screen_width
enemy3YPosition = random.randint(0, screen_height - enemy_height)

keyUp = False
keyDown = False

while 1:
    screen.fill(0)
    screen.blit(player, (playerXPosition, playerYPosition))
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))

    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True

                if event.type == pygame.KEYUP:

                    if event.key == pygame.K_UP:
                        keyUp = False
                        if event.key == pygame.K_DOWN:
                            keyDown = False

    if keyUp == True:
        if playerYPosition > 0:  #
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - image_height:
            playerYPosition += 1

    playerBox = pygame.Rect(player.get_rect())

    playerBox.top = playerYPosition
    playerBox.left = playerXPosition

    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1YPosition
    enemy1Box.left = enemy1XPosition

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition

    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition

    if playerBox.colliderect(enemy1Box):
        print("Try again!")

    elif playerBox.colliderect(enemy2Box):
        print("You lose!")

    else:
        playerBox.colliderect(enemy3Box)
        print("You lose!")

        pygame.quit()
        exit(0)

    if enemyXPosition < 0 - enemy_width:
        print("You win!")

        pygame.quit()

        exit(0)

    enemy1XPosition -= 0.15

    enemy2XPosition -= 0.20

    enemy2XPosition -= 0.25




