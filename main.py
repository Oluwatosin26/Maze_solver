from graphics import Window, Line, Point, Cell

def main():
    win = Window(800, 600)

    c = Cell(win)
    c.has_left_wall = True
    c.has_right_wall = True
    c.draw(50, 50, 100, 100)

    # c = Cell(win)
    # c.has_right_wall = False
    # c.draw(125, 125, 200, 200)

    # c = Cell(win)
    # c.has_bottom_wall = False
    # c.draw(225, 225, 250, 250)

    # c = Cell(win)
    # c.has_top_wall = False
    # c.draw(300, 300, 500, 500)

    n = Cell(win)
    n.has_left_wall = True
    n.has_right_wall = True
    n.has_top_wall = True
    n.has_bottom_wall = False
    n.draw(300, 300, 500, 500)
    #win.wait_for_close()
    # l = Line(Point(50, 50), Point(400, 400))
    # l2 = Line(Point(100, 100), Point(300, 430))
    # win.draw_line(l, "black")
    # win.draw_line(l2, "red")
    win.wait_for_close()

if __name__ == '__main__':
    main()
