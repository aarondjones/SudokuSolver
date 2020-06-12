# start main program
DIGITS = list(range(1, 10))

# create emtpy puzzle
grid = [[0 for i in range(9)] for j in range(9)]

# hard coded puzzle from North Haven Courier
grid[0][0] = 1; grid[0][3] = 6; grid[0][5] = 5; grid[0][6] = 4; grid[0][8] = 3; grid[1][0] = 6; grid[1][2] = 7;
grid[1][4] = 2; grid[1][7] = 1; grid[2][1] = 4; grid[2][4] = 7; grid[2][6] = 2; grid[4][4] = 5; grid[4][5] = 3;
grid[4][7] = 4; grid[5][2] = 4; grid[5][4] = 8; grid[5][5] = 1; grid[5][6] = 9; grid[5][8] = 7; grid[6][0] = 7;
grid[6][3] = 9; grid[7][1] = 9; grid[8][0] = 4; grid[8][2] = 3; grid[8][8] = 5

grid_possible = [[[] for i in range(9)] for j in range(9)]
grid_possible[0][0] = [1]
grid_possible[0][1] = [2,8]
grid_possible[0][2] = [2,8]
grid_possible[1][0] = [6]
grid_possible[1][1] = [5,8]
grid_possible[1][2] = [7]
grid_possible[2][0] = [3,5,9]
grid_possible[2][1] = [4]
grid_possible[2][2] = [5,9]



# print the full grid
print("_____ Unsolved Puzzle _____")
for y in grid:
    print(y)

def get_sub_grid_coords(a, b):
    # compose list of tubles that make up this sub-grid 
    sub_grid_positions = []
    for u in range(3):
        for p in range(3):
            this_pos = ((a * 3 + u), (b * 3 + p))
            sub_grid_positions.append(this_pos)    

    return sub_grid_positions



############### Main


    
#    for x in range(3):
#        for y in range(3):
x = 0
y = 0
frequency_tbl = [[] for num in range(10)]
this_sub_grid = get_sub_grid_coords(x, y)
for box in this_sub_grid:
    a = box[0]
    b = box[1]
    these_possible = grid_possible[a][b]
    print(a, b, str(these_possible))
        
    # if the box isn't solved, then there are more than one possibilities
    if len(these_possible) > 1:
        for value in these_possible:
            coordinate = (a, b)
            # put the coorindates of the box in the correct frequency bucket
            frequency_tbl[value].append(coordinate)


print(frequency_tbl)
i = 0
for coord_list in frequency_tbl:
    if len(coord_list) == 1:
        print("box: " + str(coord_list) + " is " + str(i))
        # write value back to box
        #solve_it = True
    i+=1
        
    
    
    
    
    
    
    
    
