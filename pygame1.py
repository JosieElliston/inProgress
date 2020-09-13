import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Hello World")

class box(object):
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
	def a(self):
		return self.y
	def b(self):
		return self.x + self.width
	def c(self):
		return self.y + self.height
	def d(self):
		return self.x
			

	
def colliding(box1, box2):
	if (box1.a() == box2.c() or box1.c() == box2.a()) and (box2.d() <= box1.b() <= box2.b() or box2.d() <= box1.d() <= box2.b()):
		return "collide on y"
	
	if (box1.d() == box2.b() or box1.b() == box2.d()) and (box2.a() <= box1.c() <= box2.c() or box2.a() <= box1.a() <= box2.c()):
		return "collide on x"
	
	return 0

objects = [box(0, 495, 500, 10), box(400, 300, 100, 200), box(0, 0, 10, 500), box(0, 400, 200, 50)]
player = box(250, 450, 20, 30)

xvel = 0
yvel = 0

run = True
while run:
	pygame.time.delay(10)
	win.fill((0,0,0))
	
	keys = pygame.key.get_pressed()
	
	
	collidedony = False
	
	if keys[pygame.K_LEFT]:
		if xvel > -10:
			xvel -= 1
	if keys[pygame.K_RIGHT]:
		if xvel < 10:
			xvel += 1
	for i in range(abs(int(xvel))):
		
		sign = xvel >= 0
		
		for box in objects:
			
			temp = colliding(player, box)
			if temp == "collide on x":
				player.x -= 2*(sign*2-1)
				xvel *= -.9				
				break
				
			
		player.x += (sign*2-1)
	
	for i in range(abs(int(yvel))):
		sign = yvel >= 0
		
		
		for box in objects:
			temp = colliding(player, box)
			if temp == "collide on y":
				collidedony = True
				player.y -= 2*(sign*2-1)
				yvel *= -.4
				if keys[pygame.K_UP]:
					yvel = -15
				break
				
				

			
						
		player.y += (sign*2-1)
	
	
	
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	
		
	for box in objects:
		pygame.draw.rect(win, (255,255,255), (box.x, box.y, box.width, box.height))


	
	
	xvel *= .9
	yvel += 1
		
	
	
	pygame.draw.rect(win, (255,255,255), (player.x, player.y, player.width, player.height))
	pygame.display.update()

			
pygame.quit()