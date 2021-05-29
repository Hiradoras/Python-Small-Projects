import time

DEAD = False
FINISHED = False
STEPS = 0
maze = [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,3],
        [1,0,1,0,1,0,1],
        [0,0,1,0,0,0,1],
        [1,0,1,0,1,0,1],
        [1,0,0,0,0,0,1],
        [1,2,1,0,1,0,1]]
print("Welcome to the game!+\nYou need to reach to 3 to finish the maze."+
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

    print(curr_x, curr_y)

    maze[old_y][old_x] = 0

    if curr_y < 0 or curr_y > len(maze) - 1 or curr_x < 0 or curr_x > len(maze) -1 or maze[curr_y][curr_x]==1:
        maze[curr_y][curr_x] = "X"
        print("Game Over!")
        DEAD = True
    
    if maze[curr_y][curr_x] == 3:
        maze[curr_y][curr_x] = "X"
        print(f"\nCongrats! You've made in!\nYou've completed the maze in {STEPS} step(s)")
        FINISHED = True

    if maze[curr_y][curr_x] == 0:
        maze[curr_y][curr_x] = 2
        
    for i in maze:
        print(i)

    