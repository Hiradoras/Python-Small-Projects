import shutil, random, sys, time, keyboard
keyboard.press_and_release('f11')
MIN_STREAM_LENGHT = 6
MAX_STREAM_LENGHT = 14
PAUSE = 0.05
STREAM_CHARS = ['0','1']
DENSITY = 0.02

print('Digital Stream')
print('Press Ctrl + C to stop')
print('Press Alt + F4 to quit')
time.sleep(2)

WIDTH = shutil.get_terminal_size()[0]
WIDTH -= 1

columns = [0] * WIDTH

#print('debug: ',columns)
try:
	while True:
		for i in range(WIDTH):
			if columns[i] == 0:
				if random.random() <= DENSITY:
					columns[i] = random.randint(MIN_STREAM_LENGHT,MAX_STREAM_LENGHT)

			if columns[i] > 0:
				print(random.choice(STREAM_CHARS), end='')
				columns[i] -= 1
			else:
				print(' ',end='')

		print()
		sys.stdout.flush()
		time.sleep(PAUSE)
		#print(columns)
		#input('debug: ')
except KeyboardInterrupt:
	sys.exit()
	