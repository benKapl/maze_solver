from graphics import Window, Point, Line, Cell

def main():
    win = Window(800, 600)

    cell = Cell(10, 50, 10, 50)
    cell.has_right_wall = False
    win.draw_cell(cell)

    win.wait_for_close()

if __name__ == "__main__":
    main()