import pygame

pygame.mixer.init()
pygame.mixer.music.load("ex021.mp3")
pygame.mixer.music.play()
print("Playing music...")

while pygame.mixer.music.get_busy():
    pygame.time.wait(100)
