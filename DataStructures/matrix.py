class Matrix:
    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns
        self._matrix = [[0 for _ in range(columns)] for __ in range(rows)]

    def set(self, x, y, value):
        self._matrix[y - 1][x - 1] = value

    def swap_columns(self, x1, x2):
        if x1 <= self._columns and x2 <= self._columns:
            for i in range(self._rows):
                self._matrix[i][x1 - 1], self._matrix[i][x2 - 1] = self._matrix[i][x2 - 1], self._matrix[i][x1 - 1]
        else:
            raise IndexError("Index out of range")

    def swap_rows(self, y1, y2):
        if y1 <= self._rows and y2 <= self._rows:
            self._matrix[y1 - 1], self._matrix[y2 - 1] = self._matrix[y2 - 1], self._matrix[y1 - 1]
        else:
            raise IndexError("Index out of range")

    def __repr__(self):
        s = ''
        for row in range(self._rows):
            for column in range(self._columns):
                s += str(self._matrix[row][column])
                if column != self._columns - 1:
                    s += ' '

            if row != self._rows - 1:
                s += '\n'

        return s


m = Matrix(3, 3)
m.set(1, 1, 1)
m.set(2, 1, 2)
m.set(3, 1, 3)

print(m)
m.swap_rows(1, 3)
print()
print(m)
