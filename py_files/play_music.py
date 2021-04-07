import pygame, configparser

config = configparser.ConfigParser()
config.read("config.ini")
fileName = config['Audio']['fileName']


pygame.mixer.init()
pygame.mixer.music.load(fileName)
pygame.mixer.music.play(-1) # note -1 for playing in loops
while True:
    continue
