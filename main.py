from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        # Create root
        self.__root = Tk()
        self.__root.title("Maze Solver")
        # Create canvas
        self.canvas = Canvas(self.__root, {"bg": "white", "bd": f"{height}"})
        self.canvas.pack() # geometry manager
        # 
        self.is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)


    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()
    
    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()

    def close(self):
        self.is_running = False
        

if __name__ == "__main__":
    win = Window(800, 600)
    win.wait_for_close()