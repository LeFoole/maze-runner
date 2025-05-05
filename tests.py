import unittest
from window import Window
from maze import Maze
from graphics import Point

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(Point(0,0), num_rows, num_cols)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(Point(0,0), num_rows, num_cols)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )
    
    def test_maze_open_entrance_and_exit(self):
        num_cols = 2
        num_rows = 2
        m1 = Maze(Point(0,0), num_rows, num_cols)
        self.assertEqual(
            m1._cells[0][0].has_left_wall,
            False
        )
        self.assertEqual(
            m1._cells[num_rows-1][num_cols-1].has_right_wall,
            False
        )

    def test_cells_visited_status(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(Point(0,0), num_rows, num_cols)
        for row in m1._cells:
            for cell in row:
                self.assertEqual(
                    cell.visited,
                    False
                )
        

if __name__ == "__main__":
    unittest.main()