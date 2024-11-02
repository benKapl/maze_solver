from maze import Maze
from graphics import Window

class TestMaze():
    def test_maze_create_cells(self):
        win = Window(800, 600)

        num_cols = 6
        num_rows = 5
        m1 = Maze(10, 10, num_rows, num_cols, 30, 30, win)
        assert len(m1._cells) == num_cols
        assert len(m1._cells[0]) == num_rows

    def test_maze_create_cells_large(self):
        win = Window(800, 600)

        num_cols = 4
        num_rows = 3
        m1 = Maze(100, 100, num_rows, num_cols, 100, 100, win)
        assert m1._cells[0][0].has_top_wall == False
        assert m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall == False