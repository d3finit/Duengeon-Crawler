import sys
import pygame
from pygame.locals import *
from log import Log

logger = Log()

logger.db("Began PyGame initialization...")
pygame.init() 	# intitalize pygame
logger.db("Began initialized PyGame.")

logger.db("Making varibles.")
size = (
	width,
	height
) = (
	pygame.display.Info().current_w,
	pygame.display.Info().current_h
)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (
	0,
	0,
	0
)
logger.db("Made varibles.")

def main():
	global screen
	while True:
		clock.tick(60)
		# logger.db("Clock tick sucessful.")

		for event in pygame.event.get():
			if event.type == QUIT:
				logger.crit("User forced exit. Goodbye!")
				sys.exit()
			
			elif event.type == KEYDOWN:
				if event.key == K_f:
					screen = pygame.display.set_mode(size,FULLSCREEN)
				elif event.key == K_ESCAPE:
					screen = pygame.display.set_mode(size)

		screen.fill(color)
		pygame.display.flip()


if __name__ == "__main__":
	main()