from graphics import *

win = GraphWin("Circles", 300,500)

def drawCircle(x,y,radius,color):
    c = Circle(Point(x,y),radius)
    c.setFill(color)
    c.draw(win)
def drawRectangle(x,y,color):
    r = Rectangle(Point(x,y)Point(x1,y1)
    r.setFill(color)
    r.draw(win)

def main():
    fin = open("drawing.dat","r")
    code = fin.readline().strip()
    while code != '':
        if code == "circle":
            color = fin.readline().strip()
            x = int(fin.readline())
            y = int(fin.readline())
            radius = int(fin.readline())
            drawCircle(x,y,radius,color)
        code = fin.readline().strip()
        if code == "rectangle":
            color = fin.readline().strip()
            x = int(fin.readline())
            y = int(fin.readline())
            x1 = int(fin.readline())
            y1 = int(fin.readline())

            drawRectangle(x,y,color)

            

main()
win.getMouse()
win.close()
