
import pygame, sys
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from bubble_sort import bubble_sort
from cyclic_sort import cyclic_sort

#### asking the user for the particular sorting algo
arr = [400,300,277,75,10,111,121,133,337,300,69,42,40,227,201,244,200,100]
cyclic_sort_arr = [250, 300, 350, 100, 400, 200, 150]
current = 0

try:
	algo = int(input(f"""
		### Choose the sorting algorithm you would like to visualize
		--> Press 1. for Selection sort
		--> Press 2. for Insertion sort
		--> Press 3. for bubble sort
		--> Press 4. for cyclic sort
		--> Press any other key to end the program.

		====> Array {arr} will be used...
		====> If you're choosing 4., Array {cyclic_sort_arr} will be used...
		"""))

	if algo == 1:
		all_arr = selection_sort(arr)
		sorting_algorithm = "Selection Sort"
	elif algo == 2:
		all_arr = insertion_sort(arr)
		sorting_algorithm = "Insertion Sort"
	elif algo == 3:
		all_arr = bubble_sort(arr)
		sorting_algorithm = "Bubble Sort"
	elif algo == 4:
		arr = cyclic_sort_arr
		all_arr = cyclic_sort(arr)
		sorting_algorithm = "Cyclic Sort"
	else:
		sys.exit()
except:
	sys.exit()



pygame.init()
pygame.font.init()
pygame.display.set_caption(sorting_algorithm)

WIDTH, HEIGHT = 900,700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 10
CLOCK = pygame.time.Clock()


ITEM_WIDTH = WIDTH//(2*len(arr)+1)
started = False

# defining fonts
FONT = pygame.font.Font("freesansbold.ttf", 50)
HEADING = FONT.render(sorting_algorithm,True,(200,0,0))
HEADING_RECT = HEADING.get_rect()
HEADING_RECT.center = (WIDTH//2,40)

START_BTN_X, START_BTN_Y = 0,0
START_BTN_WIDTH, START_BTN_HEIGHT = 100,50
START_BTN_FONT = pygame.font.Font("freesansbold.ttf",32)
START_BTN_TEXT = START_BTN_FONT.render("Start",True,(255,255,255))
START_BTN_RECT = START_BTN_TEXT.get_rect()
START_BTN_RECT.center = ((START_BTN_X+START_BTN_WIDTH)//2, (START_BTN_Y+START_BTN_HEIGHT)//2)

ITEM_FONT = pygame.font.Font("freesansbold.ttf",ITEM_WIDTH//2)

INFO_TEXT_1 = FONT.render("Not Started...",True, (255,50,50))
INFO_TEXT_2 = FONT.render("Sorting ...",True, (50,50,255))
INFO_TEXT_3 = FONT.render("Done!!",True, (50,255,50))
INFO_RECT = INFO_TEXT_1.get_rect()
INFO_RECT.center = (WIDTH//2,550)

sort_now = 15
sort_track = sort_now

while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
			pygame.quit()
			sys.exit()
	SCREEN.fill((255,255,255))

	# displaying start btn
	if not started:
		if 100>pygame.mouse.get_pos()[0]>0 and 50>pygame.mouse.get_pos()[1]>0:
			pygame.draw.rect(SCREEN,(0,255,0),(0,0,100,50))
			if True in pygame.mouse.get_pressed():
				started = True
		else:
			pygame.draw.rect(SCREEN,(0,155,0),(0,0,100,50))
	else:
		pygame.draw.rect(SCREEN,(0,255,0),(0,0,100,50))


	SCREEN.blit(START_BTN_TEXT, START_BTN_RECT)

	# displaying heading
	SCREEN.blit(HEADING, HEADING_RECT)


	# actual visualization
	draw_start_x = ITEM_WIDTH
	for i in all_arr[current]:
		draw_start_y = 500-i
		color = (0,0,0)

		pygame.draw.rect(SCREEN,color,(draw_start_x,draw_start_y,ITEM_WIDTH,i))
		item_text = ITEM_FONT.render(str(i),True,(255,0,0))
		SCREEN.blit(item_text,(draw_start_x,draw_start_y))

		draw_start_x += (ITEM_WIDTH*2)

	if started:
		if current!=len(all_arr)-1:
			if sort_track == sort_now:
				current += 1
				sort_track = 0
			sort_track += 1
			SCREEN.blit(INFO_TEXT_2, INFO_RECT)
		else:
			SCREEN.blit(INFO_TEXT_3, INFO_RECT)
	else:
		SCREEN.blit(INFO_TEXT_1, INFO_RECT)


	CLOCK.tick(FPS)
	pygame.display.flip()