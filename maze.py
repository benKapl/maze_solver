import random
from time import sleep

from cell import Cell
from graphics import Line, Point

class Maze():
    def __init__(self, x1, y1, 
                 num_rows, num_cols, 
                 cell_size_x, cell_size_y, 
                 win, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        if seed is not None:
            random.seed(seed)
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        self._cells = [[Cell(self._win) for _ in range(self._num_rows)] for _ in range(self._num_cols)]
        if len(self._cells) is None:
            return
        for i in range(self._num_cols):
            for j in range(self._num_rows):  
                self._draw_cell(i, j)  

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            next_index_list = []

            # determine which cell(s) to visit next
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            # if there is nowhere to go from here
            # just break out
            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])
    
    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows): 
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(i=0, j=0)

    def _solve_r(self, i, j):
        self._animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True
        
        if ((i == self._num_cols - 1) and (j == self._num_rows - 1)):
            return True
        
        directions = []

        # Add valid directions, meaning :
        # - there is cell in that direction
        # - there is not wall blocking me
        # - the cell has not been visited

        # left
        if (i > 0 
            and not current_cell.has_left_wall 
            and not self._cells[i - 1][j].visited):
            directions.append((i - 1, j))
        # right
        if (i < self._num_cols - 1 
            and not current_cell.has_right_wall 
            and not self._cells[i + 1][j].visited):
            directions.append((i + 1, j))
        # up
        if (j > 0 
            and not current_cell.has_top_wall 
            and not self._cells[i][j - 1].visited):
            directions.append((i, j - 1))
        # down
        if (j < self._num_rows - 1 
            and not current_cell.has_bottom_wall 
            and not self._cells[i][j + 1].visited):
            directions.append((i, j + 1))


        # if there are no valid direction, return False
        if len(directions) == 0:
            return False

        for direction in directions: 
            futur_cell = self._cells[direction[0]][direction[1]]

            # move to futur cell
            current_cell.draw_move(futur_cell)

            # check if maze is solved. If not, undo the move recursively
            solved = self._solve_r(direction[0], direction[1])
            if solved:
                return True
            current_cell.draw_move(futur_cell, undo=True)
            








            










            


    




    



# a = ([["foo" for _ in range(3)] for _ in range(3)])
# print(len(a))
