from window import Window
from maze import Maze
from graphics import Point


def main():
    win = Window(800, 600)

    maze = Maze(Point(50,50), window=win)
    maze.solve()

    win.wait_for_close()


main()