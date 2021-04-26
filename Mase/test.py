"""Implemention of the Maze ADT using a 2-D array."""
from arrays import Array2D
from lliststack import Stack


class Maze:
    """Define constants to represent contents of the maze cells."""
    MAZE_WALL = "*"
    PATH_TOKEN = "x"
    TRIED_TOKEN = "o"

    def __init__(self, num_rows, num_cols):
        """Creates a maze object with all cells marked as open."""
        self._maze_cells = Array2D(num_rows, num_cols)
        self._start_cell = None
        self._exit_cell = None

    def num_rows(self):
        """Returns the number of rows in the maze."""
        return self._maze_cells.num_rows()

    def num_cols(self):
        """Returns the number of columns in the maze."""
        return self._maze_cells.num_cols()

    def set_wall(self, row, col):
        """Fills the indicated cell with a "wall" marker."""
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._maze_cells[row, col] = self.MAZE_WALL

    def set_start(self, row, col):
        """Sets the starting cell position."""
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._start_cell = _CellPosition(row, col)

    def set_exit(self, row, col):
        """Sets the exit cell position."""
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._exit_cell = _CellPosition(row, col)


    def find_path(self):
        """
        Attempts to solve the maze by finding a path from the starting cell
        to the exit. Returns True if a path is found and False otherwise.
        """
        path = Stack()
        i = self._start_cell.row
        j = self._start_cell.col
        counter = 0
        while True:
            check = 0
            if self._exit_found(i, j):
                for _ in range(len(path)):
                    coord = path.pop()
                    self._maze_cells[coord[0], coord[1]] = "x"
                self._maze_cells[self._exit_cell.row, self._exit_cell.col] = "x"
                return True
            if (self._valid_move(i-1, j) and self._maze_cells[i-1, j] == None and
                                                                    check == 0):
                if path.is_empty() or path.peek() != (i-1, j):
                    path.push((i, j))
                    counter = 0
                    check = 1
                    i -= 1
                elif counter == 1:
                    self._maze_cells[i, j] = "o"
                    try:
                        path.pop()
                    except AssertionError:
                        return False
                    counter = 0
                    check = 1
                    i -= 1
                else:
                    counter += 1
            if (self._valid_move(i, j+1) and self._maze_cells[i, j+1] == None
                                                            and check == 0):
                if path.is_empty() or path.peek() != (i, j+1):
                    path.push((i, j))
                    counter = 0
                    check = 1
                    j += 1
                elif counter == 1:
                    self._maze_cells[i, j] = "o"
                    try:
                        path.pop()
                    except AssertionError:
                        return False
                    counter = 0
                    check = 1
                    j += 1
                else:
                    counter += 1
            if (self._valid_move(i+1, j) and self._maze_cells[i+1, j] == None
                                                            and check == 0):
                if path.is_empty() or path.peek() != (i+1, j):
                    path.push((i, j))
                    counter = 0
                    check = 1
                    i += 1
                elif counter == 1:
                    self._maze_cells[i, j] = "o"
                    try:
                        path.pop()
                    except AssertionError:
                        return False
                    counter = 0
                    check = 1
                    i += 1
                else:
                    counter += 1
            if (self._valid_move(i, j-1) and self._maze_cells[i, j-1] == None
                                                            and check == 0):
                if path.is_empty() or path.peek() != (i, j-1):
                    path.push((i, j))
                    counter = 0
                    check = 1
                    j -= 1
                elif counter == 1:
                    self._maze_cells[i, j] = "o"
                    try:
                        path.pop()
                    except AssertionError:
                        return False
                    counter = 0
                    check = 1
                    j -= 1
                else:
                    counter += 1
            if check == 0 and counter == 0:
                return False

    def reset(self):
        """Resets the maze by removing all "path" and "tried" tokens."""
        for i in range(self.num_rows()):
            for j in range(self.num_cols()):
                if (self._maze_cells[i, j] == "x" or 
                    self._maze_cells[i, j] == "o"):
                    self._maze_cells[i, j] = None

    def __str__(self):
        """Returns a text-based representation of the maze."""
        output = ""
        for i in range(self.num_rows()):
            if i != 0:
                output += "\n"
            for j in range(self.num_cols()):
                if self._maze_cells[i, j] is not None:
                    output += f"{self._maze_cells[i, j]} "
                else:
                    output += f"_ "
        return output

    def _valid_move(self, row, col):
        """Returns True if the given cell position is a valid move."""
        return row >= 0 and row < self.num_rows() \
               and col >= 0 and col < self.num_cols() \
               and self._maze_cells[row, col] is None

    def _exit_found(self, row, col):
        """Helper method to determine if the exit was found."""
        return row == self._exit_cell.row and col == self._exit_cell.col

    def _mark_tried(self, row, col):
        """Drops a "tried" token at the given cell."""
        self._maze_cells[row, col] = self.TRIED_TOKEN

    def _mark_path(self, row, col):
        """Drops a "path" token at the given cell."""
        self._maze_cells[row, col] = self.PATH_TOKEN


class _CellPosition(object):
    """Private storage class for holding a cell position."""
    def __init__(self, row, col):
        self.row = row
        self.col = col

if __name__ == "__main__":
    maze = build_maze("mazefile.txt")
    print(maze)