import random

from pprint import pprint

from graphics import Window
from cell import Cell
from maze import Maze


def main():
    win = Window(800, 600)

    num_cols = 5
    num_rows = 5
    m1 = Maze(30, 30, num_rows, num_cols, 40, 40, win)
    # m1._break_entrance_and_exit()


    win.wait_for_close()

if __name__ == "__main__":
    win = Window(800, 600)

    num_cols = 5
    num_rows = 5
    m1 = Maze(30, 30, num_rows, num_cols, 40, 40, win)

    print(m1._random)
    # print(random.seed(3))

    # main()