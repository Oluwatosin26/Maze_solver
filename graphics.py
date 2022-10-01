from tkinter import *

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title('Maze AI')
        self.__canvas = Canvas(self.__root, bg="cyan",height=height,width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol('WM_DELETE_WINDOW', self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print('Window closed...')
    
    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

    
    def close(self):
        self.__running = False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self,p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="red"):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)
        canvas.pack(fill=BOTH, expand=1)

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y2), Point(x1,y1))
            self._win.draw_line(line, 'black')

        if self.has_right_wall:
            line = Line(Point(x2, y2), Point(x2,y1))
            self._win.draw_line(line, 'black')

        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2,y1))
            self._win.draw_line(line, 'black')

        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2,y2))
            self._win.draw_line(line, 'black')


