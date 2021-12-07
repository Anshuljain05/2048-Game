import random
def start_game():
    mat = []
    for i in range(4):
        mat.append([0]*4)
    return mat

def add_new_2(mat):
    r = random.randint(0,3)
    c = random.randint(0,3)
    
    while mat[r][c] != 0:
    	r = random.randint(0,3)
    	c = random.randint(0,3)
    mat[r][c] = 2
    return mat

def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][4-j-1])
    return new_mat

def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat

def compress(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([0]*4)
    
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                pos += 1
    return new_mat

def merge(mat):
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
                mat[i][j] = mat[i][j]*2
                mat[i][j+1] = 0
    return mat

def get_current_state(mat):
    #Anywhere 2048 is present
    for i in range(4):
        for j in range(4):
            if(mat[i][j] == 2048):
                return "WON"
    
    #Anywhere 0 is present
    for i in range(4):
        for j in range(4):
            if(mat[i][j] == 0):
                return "GAME NOT OVER"
    
    #Every row and column except last row and last column
    for i in range(3):
        for j in range(3):
            if(mat[i][j] == mat[i][j+1] or mat[i][j] == mat[i+1][j]):
                return "GAME NOT OVER"
    
    #Last row
    for j in range(3):
        if(mat[3][j] == mat[3][j+1]):
            return "GAME NOT OVER"
    
    #Last column
    for i in range(3):
        if(mat[i][3] == mat[i+1][3]):
            return "GAME NOT OVER"
    
    return "LOST"

def move_up(grid):
    transposed_grid = transpose(grid)
    new_grid = compress(transposed_grid)
    new_grid = merge(new_grid)
    new_grid = compress(new_grid)
    final_grid = transpose(new_grid)
    
    return final_grid


def move_down(grid):
    transposed_grid = transpose(grid)
    reversed_grid = reverse(transposed_grid)
    new_grid = compress(reversed_grid)
    new_grid = merge(new_grid)
    new_grid = compress(new_grid)
    reversed_grid = reverse(new_grid)
    final_grid = transpose(reversed_grid)
    
    return final_grid

def move_right(grid):
    #Implement This Function
    reversed_grid = reverse(grid)
    new_grid = compress(reversed_grid)
    new_grid = merge(new_grid)
    new_grid = compress(new_grid)
    final_grid = reverse(new_grid)
    
    return final_grid

def move_left(grid):
    new_grid = compress(grid)
    new_grid = merge(new_grid)
    new_grid = compress(new_grid)
    
    return new_grid

def printBox(mat):
    print()
    for row in mat:
        for cell in row:
            print(cell,end="\t")
        print()
        print()

def intro():
    mat = start_game()
    mat[1][3] = 2
    mat[2][2] = 2
    mat[3][0] = 4
    mat[3][1] = 8
    mat[2][1] = 4

    print("\nWelcome to 2048 Game!")
    print("Instructions:")
    print("To move up: Enter 8")
    print("To move down: Enter 5")
    print("To move left: Enter 4")
    print("To move right: Enter 6")
    
    print()
    print("Now Let's Play!")
    printBox(mat)
    return mat


toContinue = "Y"
mat = intro()
while(toContinue != "N"):
    
    if(get_current_state(mat) == "GAME NOT OVER"):
        print("Enter direction digit: ")
        direction = int(input())
        if direction == 8:
            mat = move_up(mat)
        elif direction == 5:
            mat = move_down(mat)
        elif direction == 4:
            mat = move_left(mat)
        elif direction == 6:
            mat = move_right(mat)
        else:
            print("Invalid Direction Digit!")
        mat = add_new_2(mat)
        printBox(mat)
    elif(get_current_state(mat) == "WON"):
        print("YOU WON!!!")
    elif(get_current_state(mat) == "LOST"):
        print("YOU LOST! BETTER LUCK NEXT TIME!")
        print("Do You Want to Play Again!(Y/N)")
        toContinue = input()
        if toContinue == "N":
            print("See You Again Later!")
        else:
            mat = intro()
