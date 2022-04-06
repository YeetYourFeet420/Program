import os
from operator import truediv
import pygame
pygame.init()
from time import sleep
window = pygame.display.set_mode((500,500))

should_continue = True
while should_continue == True:
    pygame.display.flip()
    troubles = pygame.event.get()
    print(troubles)
    sleep(0.1)
    for trouble in troubles:
        if trouble.type == pygame.QUIT:
            os.exit()