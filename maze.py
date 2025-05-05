from cell import Cell
from graphics import Point
import time, random

class Maze:
    ''

    def __init__(self, origin, num_rows=10, num_cols=15, window=None, seed=None):
        self._win = window
        self.__origin = origin
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self._cells = []

        random.seed(seed)

        self._create_cells()

    def _create_cells(self):
        for row in range(self.__num_rows):
            self._cells.append([])
            for col in range(self.__num_cols):
                # Cell Origin = Maze Origin + row_n*Cell.__edge_lenght
                cell_origin = Point(self.__origin.x + col*Cell.get_lenght(), self.__origin.y + row*Cell.get_lenght())
                self._cells[row].append(Cell(cell_origin, window=self._win))
                self._draw_cell(row, col)
        
        self._break_entrance_and_exit()
        for i in range(self.__num_rows):
            for j in range(self.__num_cols):
                self._break_walls_r(i,j)

        self._reset_cells_visited()


    def _draw_cell(self, row, col):
        if self._win is None:
            return

        self._cells[row][col].draw()
        self._animate()


    def _animate(self):
        if self._win is None:
            return

        self._win.redraw()
        time.sleep(0.005)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._draw_cell(0, 0)

        self._cells[-1][-1].has_right_wall = False
        self._draw_cell(-1, -1)

    def _break_walls_r(self, row, col):
        #if self._cells[row][col].visited == True:
        #    return

        self._cells[row][col].visited = True
        available_cells = self._check_available_adjacent_cells(row, col)
        if len(available_cells) == 0:
            return
        
        next_cell = self._pick_random_cell(available_cells)
        self._break_wall_between((row,col), next_cell)
        self._draw_cell(row, col)

        self._break_walls_r(next_cell[0], next_cell[1])

    def _check_available_adjacent_cells(self, row, col):
        to_check = [(row,col-1), (row,col+1), (row-1, col), (row+1, col)]
        available_cells = []

        for pos in to_check:
            if self.__is_out_of_bounds(pos[0], pos[1]):
                continue

            if not self._cells[pos[0]][pos[1]].visited:
                available_cells.append(pos)

        return available_cells
    
    def _pick_random_cell(self, available_cells):
        return available_cells[random.randrange(len(available_cells))]
    
    def _break_wall_between(self, cell_coord_1, cell_coord_2):
        direction = (cell_coord_1[0]-cell_coord_2[0], cell_coord_1[1]-cell_coord_2[1])
        match direction:
            case (0,-1):
                self._cells[cell_coord_1[0]][cell_coord_1[1]].has_right_wall = False
                self._cells[cell_coord_2[0]][cell_coord_2[1]].has_left_wall = False
            case (0,1):
                self._cells[cell_coord_1[0]][cell_coord_1[1]].has_left_wall = False
                self._cells[cell_coord_2[0]][cell_coord_2[1]].has_right_wall = False
            case (-1,0):
                self._cells[cell_coord_1[0]][cell_coord_1[1]].has_bot_wall = False
                self._cells[cell_coord_2[0]][cell_coord_2[1]].has_top_wall = False
            case (1,0):
                self._cells[cell_coord_1[0]][cell_coord_1[1]].has_top_wall = False
                self._cells[cell_coord_2[0]][cell_coord_2[1]].has_bot_wall = False
            case _:
                print("Bad Math!")


    def __is_out_of_bounds(self, i, j):
        return (i < 0 or i >= self.__num_rows) or (j < 0 or j >= self.__num_cols)

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def solve(self):
        if self._solve_r(0, 0):
            print("SOLVED!")
        else:
            print("wompwompwomp")

    def _solve_r(self, row, col):
        self._animate()

        if row == self.__num_rows-1 and col == self.__num_cols-1:
            return True

        current_cell = self._cells[row][col]
        current_cell.visited = True
        #Go right
        if self.__can_go_right_from(row, col):
            current_cell.draw_move(self._cells[row][col+1])
            if self._solve_r(row, col+1):
                return True
            #elif not self.__is_out_of_bounds(row, col+1) and self._cells[row][col+1].visited:
            else:
                current_cell.draw_move(self._cells[row][col+1], True)

        #Go left
        if self.__can_go_left_from(row, col):
            current_cell.draw_move(self._cells[row][col-1])
            if self._solve_r(row, col-1):
                return True
            elif not self.__is_out_of_bounds(row, col-1) and self._cells[row][col-1].visited:
                current_cell.draw_move(self._cells[row][col-1], True)
        
        #Go Top
        if self.__can_go_up_from(row, col):
            current_cell.draw_move(self._cells[row-1][col])
            if self._solve_r(row-1, col):
                return True
        #elif not self.__is_out_of_bounds(row-1, col) and self._cells[row-1][col].visited:
            else:
                current_cell.draw_move(self._cells[row-1][col], True)

        #Go bot
        if self.__can_go_down_from(row, col):
            current_cell.draw_move(self._cells[row+1][col])
            if self._solve_r(row+1, col):
                return True
        #elif not self.__is_out_of_bounds(row+1, col) and self._cells[row+1][col].visited:
            else:
                current_cell.draw_move(self._cells[row+1][col], True)
        
        return False
    
    def __can_go_right_from(self, row, col):
        return (not self.__is_out_of_bounds(row, col+1) and
                not self._cells[row][col].has_right_wall and 
                not self._cells[row][col+1].has_left_wall and 
                not self._cells[row][col+1].visited)

    def __can_go_left_from(self, row, col):
        return (not self.__is_out_of_bounds(row, col-1) and
                not self._cells[row][col].has_left_wall and 
                not self._cells[row][col-1].has_right_wall and 
                not self._cells[row][col-1].visited)
    
    def __can_go_up_from(self, row, col):
        return (not self.__is_out_of_bounds(row-1, col) and
                not self._cells[row][col].has_top_wall and 
                not self._cells[row-1][col].has_bot_wall and 
                not self._cells[row-1][col].visited)
    
    def __can_go_down_from(self, row, col):
        return (not self.__is_out_of_bounds(row+1, col) and
                not self._cells[row][col].has_bot_wall and 
                not self._cells[row+1][col].has_top_wall and 
                not self._cells[row+1][col].visited)