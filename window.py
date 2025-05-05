from tkinter import Tk, BOTH, Canvas
from graphics import Line

class Window:
    ''

    def __init__(self, width, height):
        self.width = width
        self.height = height

        #__rootWidget as private member
        self.__rootWidget = Tk()
        self.__rootWidget.title("Hardcoded")
        self.__rootWidget.geometry(str(width)+"x"+str(height))
        self.__rootWidget.minsize(width,height)
        #Connect the close method to the "delete window" action. 
        #This will stop the program from running when the graphical window is closed.
        self.__rootWidget.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas(self.__rootWidget, width=width, height=height, bg='white')
        self.__canvas.pack()
        self.__isRunning = False


    def redraw(self):
        self.__rootWidget.update_idletasks()
        self.__rootWidget.update()

    def wait_for_close(self):
        self.__isRunning = True

        while( self.__isRunning ):
            self.redraw()

    def get_canvas(self):
        return self.__canvas

    def close(self):
        self.__isRunning = False

    def draw_line(self, line, color="black"):
        line.draw(self.__canvas, color)
