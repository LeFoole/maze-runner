from graphics import Point, Line

class Cell:
    ''
    __edge_lenght = 46

    def __init__(self, origin: Point, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bot_wall=True, window=None):
        self._origin = origin
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bot_wall = has_bot_wall
        self.visited = False
        self._win = window

    def get_origin(self):
        return self._origin
    
    @classmethod
    def get_lenght(self):
        return self.__edge_lenght

    @property
    def center(self):
        return Point(self._origin.x+self.__edge_lenght/2, self._origin.y+self.__edge_lenght/2)

    def draw(self):
        if self._win is None:
            return 
            
        line = Line(Point(0,0), Point(0,0))

        #Left wall
        line.set_origin(self._origin)
        line.set_end( Point(self._origin.x, self._origin.y+Cell.__edge_lenght) )
        self._win.draw_line(line, "black" if self.has_left_wall else "white")    
        
        #Right wall
        line.set_origin( Point(self._origin.x+Cell.__edge_lenght, self._origin.y) )
        line.set_end( Point(self._origin.x+Cell.__edge_lenght, self._origin.y+Cell.__edge_lenght) )
        self._win.draw_line(line, "black" if self.has_right_wall else "white")

        #Top wall
        line.set_origin( Point(self._origin.x, self._origin.y) )
        line.set_end( Point(self._origin.x+Cell.__edge_lenght, self._origin.y) )
        self._win.draw_line(line, "black" if self.has_top_wall else "white")
        
        #Bot Wall
        line.set_origin( Point(self._origin.x, self._origin.y+Cell.__edge_lenght) )
        line.set_end( Point(self._origin.x+Cell.__edge_lenght, self._origin.y+Cell.__edge_lenght) )
        self._win.draw_line(line, "black" if self.has_bot_wall else "white")

    def draw_move(self, to_cell, undo=False):
        color = "gray" if undo else "red"
        line = Line(self.center, to_cell.center)
        self._win.draw_line(line, color)

    def set_walls(self, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bot_wall=True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bot_wall = has_bot_wall