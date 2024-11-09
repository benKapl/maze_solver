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
        current = self._cells[i][j]
        current.visited = True

        while True:
            adjacent_cells = []
            directions = []

            # Check all boundaries:
            if i + 1 < self._num_cols:
                adjacent_cells.append(self._cells[i+1][j])
                directions.append((i+1, j))
            if i - 1 >= 0:
                adjacent_cells.append(self._cells[i-1][j])
                directions.append((i-1, j))
            if j + 1 < self._num_rows:
                adjacent_cells.append(self._cells[i][j+1])
                directions.append((i, j+1))
            if j - 1 < 0:
                adjacent_cells.append(self._cells[i][j-1])
                directions.append((i, j-1))

            visitable_cells = [cell for cell in adjacent_cells if not cell.visited]

            if not visitable_cells:
                current._draw_cell()
                return
            
            # if some adjacent_cells are visitable : break wall and go to it
            direction = random.choice(directions)

            if direction == (i+1, j):
                current.has_right_wall = False
            if direction == (i-1, j):
                current.has_left_wall = False
            if direction == (i, j+1):
                current.has_bottom_wall = False
            if direction == (i, j-1):
                current.has_top_wall = False

            self._break_walls_r(*direction)

            










            


    




    



# a = ([["foo" for _ in range(3)] for _ in range(3)])
# print(len(a))
