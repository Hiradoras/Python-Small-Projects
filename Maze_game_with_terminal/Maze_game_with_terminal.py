import time, sys

DEAD = False
FINISHED = False
OUT_OF_MAZE = False
WAIT_TIME = 1.3


STEPS = 0

maze = [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,3],
        [1,0,1,0,1,0,1],
        [0,0,1,0,0,0,1],
        [1,0,1,0,1,0,1],
        [1,0,0,0,0,0,1],
        [1,2,1,0,1,0,1]]
print("Welcome to the game!\nYou need to reach to 3 to finish the maze."+
    "\nIf you touch the walls you are dead!\nUse W,A,S,D to move."+
    "\nYour current location is symbolized with '2'")
print("\nCurrent situation below: ")
for i in maze:
    print(i)
curr_x = 0
curr_y = 0
for y in range(len(maze)):
        for x in range(len(maze)):
            if maze[x][y] == 2:
                curr_x,curr_y = y, x
                old_x = curr_x
                old_y = curr_y

while not DEAD and not FINISHED:
    STEPS += 1
    old_x, old_y = curr_x,curr_y
    direct = input("Move!>").lower()
    if direct == 'w': 
        curr_y -= 1
    if direct == 's': 
        curr_y += 1
    if direct == 'a': 
        curr_x -= 1
    if direct == 'd': 
        curr_x += 1

    if curr_y < 0 or curr_y > len(maze) - 1 or curr_x < 0 or curr_x > len(maze) -1:
        OUT_OF_MAZE = True

    if not OUT_OF_MAZE:
        maze[old_y][old_x] = 0

    if not OUT_OF_MAZE and maze[curr_y][curr_x] == 0:
        maze[curr_y][curr_x] = 2

    if OUT_OF_MAZE:
        maze[old_y][old_x] = 'X'
        print("Game Over!\nYou are out of maze!")
        print("####################################")
        time.sleep(WAIT_TIME)
        DEAD = True
        break

    if not OUT_OF_MAZE and maze[curr_y][curr_x]==1:
        maze[curr_y][curr_x] = "X"
        print("Game Over!")
        print("####################################")
        time.sleep(WAIT_TIME)
        DEAD = True
        break

    if not OUT_OF_MAZE and maze[curr_y][curr_x] == 3:
        maze[curr_y][curr_x] = "X"
        print(f"\nCongrats! You've made in!\nYou've completed the maze in {STEPS} steps")
        print("####################################")
        time.sleep(WAIT_TIME)
        FINISHED = True
        break

    for i in maze:
        print(i)

try:
    while True:
        print("Press  Ctrl + C to quit!\n")
        for i in maze:
            print(i)
        time.sleep(1)
except KeyboardInterrupt:
    sys.exit()
