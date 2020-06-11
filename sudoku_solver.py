
def get_column(matrix, n):
    col = []
    for row in matrix:
        col.append(row[n])
    col = [x for x in col if x != 0]
    col.sort()
    return col

def get_row(matrix, n):
    row = []
    row = matrix[n]
    row = [x for x in row if x != 0]
    row.sort()
    return row

def get_sub_grid_coords(a, b):
    # compose list of tubles that make up this sub-grid 
    sub_grid_positions = []
    for u in range(3):
        for p in range(3):
            this_pos = ((a * 3 + u), (b * 3 + p))
            sub_grid_positions.append(this_pos)    

    return sub_grid_positions


def get_sub_grid(matrix, x, y):
    """
    pass in the full puzzle and a (x, y) tuple
    get back a list of the values in that sub-group
    """
    sub_grid = []

    # find which sub-grid to create using floor division
    m = x // 3
    n = y // 3
        
    # compose list of tubles that make up this sub-grid 
    sub_positions = get_sub_grid_coords(m, n)
    
    # pull values for sub_grid from the table
    for position in sub_positions:
        sub_grid.append(matrix[position[0]][position[1]])
    
    # remove zeros and sort list
    sub_grid = [x for x in sub_grid if x != 0]
    sub_grid.sort()
    return sub_grid


def get_sub_grid_coords(a, b):
    # compose list of tubles that make up this sub-grid 
    sub_grid_positions = []
    for u in range(3):
        for p in range(3):
            this_pos = ((a * 3 + u), (b * 3 + p))
            sub_grid_positions.append(this_pos)    

    return sub_grid_positions


# start main program
DIGITS = list(range(1, 10))

# create emtpy puzzle
grid = [[0 for i in range(9)] for j in range(9)]
grid_possible = [[[] for i in range(9)] for j in range(9)]

# # hard coded puzzle from Wikipedia
# grid[0][0] = 5; grid[0][1] = 3; grid[0][4] = 7; grid[1][0] = 6; grid[1][3] = 1; grid[1][4] = 9; grid[1][5] = 5;
# grid[2][1] = 9; grid[2][2] = 8; grid[2][7] = 6; grid[3][0] = 8; grid[3][4] = 6; grid[3][8] = 3; grid[4][0] = 4;
# grid[4][3] = 8; grid[4][5] = 3; grid[4][8] = 1; grid[5][0] = 7; grid[5][4] = 2; grid[5][8] = 6; grid[6][1] = 6;
# grid[6][6] = 2; grid[6][7] = 8; grid[7][3] = 4; grid[7][4] = 1; grid[7][5] = 9; grid[7][8] = 5; grid[8][4] = 8;
# grid[8][7] = 7; grid[8][8] = 9

# hard coded puzzle from North Haven Courier
grid[0][0] = 1; grid[0][3] = 6; grid[0][5] = 5; grid[0][6] = 4; grid[0][8] = 3; grid[1][0] = 6; grid[1][2] = 7;
grid[1][4] = 2; grid[1][7] = 1; grid[2][1] = 4; grid[2][4] = 7; grid[2][6] = 2; grid[4][4] = 5; grid[4][5] = 3;
grid[4][7] = 4; grid[5][2] = 4; grid[5][4] = 8; grid[5][5] = 1; grid[5][6] = 9; grid[5][8] = 7; grid[6][0] = 7;
grid[6][3] = 9; grid[7][1] = 9; grid[8][0] = 4; grid[8][2] = 3; grid[8][8] = 5

# # hard coded puzzle from North Haven Citizen
# grid[0][3] = 8; grid[1][3] = 7; grid[1][6] = 4; grid[1][7] = 9; grid[2][1] = 3; grid[2][3] = 5; grid[2][5] = 9;
# grid[2][6] = 2; grid[2][7] = 6; grid[3][0] = 8; grid[3][6] = 6; grid[3][7] = 2; grid[4][1] = 7; grid[4][6] = 5;
# grid[5][1] = 5; grid[5][2] = 1; grid[5][5] = 4; grid[6][5] = 6; grid[6][7] = 1; grid[7][4] = 9; grid[7][7] = 5;
# grid[7][8] = 2; grid[8][0] = 4; grid[8][2] = 2; grid[8][4] = 1;


# print the full grid
print("_____ Unsolved Puzzle _____")
for y in grid:
    print(y)

solve_it = True
while solve_it:
    found_one = False    
    # look for elimination finds
    i = 0 
    for row in grid:
        j = 0
        for x in row:
            this_box = grid[i][j]
            #print(str(i) + str(j) + "this_box: " + str(this_box))
            if this_box == 0:
                this_row = get_row(grid, i)
                this_col = get_column(grid, j)
                this_sub_grid = get_sub_grid(grid, i, j)
                used_numbers = this_row + this_col + this_sub_grid

                possible = []
                for x in DIGITS:
                    if x not in used_numbers:
                        possible.append(x)
                print(str(i)+ " " + str(j) +" possible: " + str(possible))
                grid_possible[i][j] = possible

                if len(possible) == 1:
                    found_one = True
                    print("Box " + str(i) + ", " + str(j) + " is " + str(possible[0]))
                    grid[i][j] = possible[0]
            else:
                grid_possible[i][j] = this_box
            
            j+=1        
        i+=1



    # look for unique possibilites
    for x in range(3):
        for y in range(3):
    
            frequency_tbl = [[] for num in range(10)]
            this_sub_grid = get_sub_grid_coords(x, y)
            for box in this_sub_grid:
                a = box[0]
                b = box[1]
                these_possible = grid_possible[a][b]
                print(str(these_possible))
        
#             # if the box isn't solved, then there are more than one possibilities
#             if len(these_possible) > 1:
#                 for value in these_possible:
#                     coordinate = (a, b)
#                     # put the coorindates of the box in the correct frequency bucket
#                     frequency_tbl[value].append(coordinate)
# 
# 
#         print(frequency_tbl)
#         i = 0
#         for coord_list in frequency_tbl:
#             if len(coord_list) == 1:
#                 print("box: " + str(coord_list) + " is " + str(i))
#                 # write value back to box
#                 a = coord_list[0]
#                 b = coord_list[1]
#                 grid[a][b] = i
#                 grid_possible[a][b] = [i]
#                 solve_it = True
#             i+=1
#     


    if not found_one:
        solve_it = False


print("_____ Solved Puzzle _____")
for y in grid:
    print(y)