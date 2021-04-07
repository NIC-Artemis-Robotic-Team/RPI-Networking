import pygame, configparser
# ffplay -nodisp -volume 100 -loop 0 song.mp3
config = configparser.ConfigParser()
config.read("config.ini")
fileName = config['Audio']['fileName']

print(fileName)

pygame.mixer.init()
pygame.mixer.music.load(fileName)
pygame.mixer.music.play() # note -1 for playing in loops
while True:
    continue
# do whatever
# when ready to stop do:
# pygame.mixer.pause()