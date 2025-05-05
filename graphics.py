class Point:
    ''

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    ''

    def __init__(self, origin: Point, end: Point):
        self.origin = origin
        self.end = end

    def draw(self, canvas, color):
        canvas.create_line(self.origin.x, self.origin.y, self.end.x, self.end.y, fill=color, width=2)

    def set_origin(self, origin: Point):
        self.origin = origin

    def set_end(self, end: Point):
        self.end = end