import pygame

pygame.init()
win = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("5")




def f(x):
	return x**2

def point(x, y):
#	pygame.draw.rect(win, (255,255,255), (x+500, -y, 10, 10))
	pygame.draw.circle(win, (255,255,255), (x+500, -y, 10, 10), 0)




win.fill((0,0,0))


for x in range(-500, 500):
	point(x, f(x))

	





pygame.display.update()

print("done")