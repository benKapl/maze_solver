from time import sleep

from cell import Cell

class Maze():
    def __init__(self, x1, y1, 
                 num_rows, num_cols, 
                 cell_size_x, cell_size_y, 
                 win,):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        self._cells = [[Cell(self._win) for _ in range(self._num_cols)] for _ in range(self._num_rows)]
        if len(self._cells) is None:
            return
        for i in range(self._num_rows):
            for j in range(self._num_cols):  
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

    



# a = ([["foo" for _ in range(3)] for _ in range(3)])
# print(len(a))