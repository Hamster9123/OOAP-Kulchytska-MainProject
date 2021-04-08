import math
import csv
import timeit
import time


class Matrix:
    def __init__(self, value=None):
        self._data = value

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.get_shape() == other.get_shape():
                result = []
                rows, cols = self.get_shape()
                for row in range(rows):
                    result.append([])
                    for col in range(cols):
                        result[row].append(self[row][col] * other[row][col])
                return Matrix(result)
            else:
                raise ValueError("Matrixes have different shape")
        elif isinstance(other, int) or isinstance(other, float):
            result = []
            rows, cols = self.get_shape()
            for row in range(rows):
                result.append([])
                for col in range(cols):
                    result[row].append(self[row][col] * other)
            return Matrix(result)
        else:
            raise ValueError("Incorrect argument type")

    def __matmul__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Incorrect argument type")

        result = []
        rows1, cols1 = self.get_shape()
        rows2, cols2 = other.get_shape()

        if cols1 != rows2:
            raise ValueError("Matrix have different length of column and rows")

        for row in range(rows1):
            result.append([])
            for col in range(cols2):
                for k in range(cols1):
                    if len(result[row]) == col:
                        result[row].append(self[row][k] * other[k][col])
                    else:
                        result[row][col] += self[row][k] * other[k][col]
        return result

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False

        if self.get_shape() != other.get_shape():
            return False

        rows, cols = self.get_shape()
        for row in range(rows):
            for col in range(cols):
                if self[row][col] != other[row][col]:
                    return False
        return True

    def __getitem__(self, item):
        return self._data[item]

    def __str__(self):
        res = '['
        is_first = True
        for row in self._data:
            if is_first:
                is_first = False
            else:
                res += '\n'
            res += '[ '
            for item in row:
                res += str(item) + ' '
            res += ']'
        res += ']'
        return res

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.get_shape() == other.get_shape():
                result = []
                rows, cols = self.get_shape()
                for row in range(rows):
                    result.append([])
                    for col in range(cols):
                        result[row].append(self[row][col] + other[row][col])
                return Matrix(result)
            else:
                raise ValueError("Matrixes have different shape")
        elif isinstance(other, int) or isinstance(other, float):
            result = []
            rows, cols = self.get_shape()
            for row in range(rows):
                result.append([])
                for col in range(cols):
                    result[row].append(self[row][col] + other)
            return Matrix(result)
        else:
            raise ValueError("Incorrect argument type")

    @staticmethod
    def sum(m1, m2):
        return m1 + m2

    @staticmethod
    def read_csv(path):
        with open(path, 'r') as f:
            # reader = csv.reader(f)
            # data = []
            # for row in reader:
            #     if len(row) == 0:
            #         continue
            #     data.append([float(i) for i in row])
            data = [[float(i) for i in row] for row in csv.reader(f) if len(row) != 0]
            return Matrix(data)

    def write_csv(self, path):
        with open(path, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(self._data)

    def sqrt(self):
        result = []
        rows, cols = self.get_shape()
        for row in range(rows):
            result.append([])
            for col in range(cols):
                result[row].append(math.sqrt(self[row][col]))
        return Matrix(result)

    def trans(self):
        result = []
        rows, cols = self.get_shape()
        for col in range(cols):
            result.append([])
            for row in range(rows):
                result[col].append(self[row][col])
        return Matrix(result)

    def get_shape(self):
        rows = len(self._data) if self._data is not None else 0
        cols = len(self._data[0]) if rows > 0 else 0

        return rows, cols


def main():
    l = [[1, 2, 3], [5, 4, 6], [7, 8, 9]]
    a = Matrix(l)
    b = Matrix(l)
    c = Matrix()
    shape = a.get_shape()
    print(shape)
    print(b.get_shape())
    print(c.get_shape())
    print('\n')
    start = time.time()
    temp = a + b
    end = time.time()
    print(f"operation a + b takes {(end - start) * 1_000_000} microseconds")
    print(temp)
    # print('\n')
    # print(a + 7)
    # print('\n')
    # print(a + 7.9)
    # print('\n')
    # print(a.sqrt())
    # print('\n')
    # print(a.trans())
    # print('\n')
    # print(a == b)
    # print('\n')
    # print(a == c)
    # print('\n')
    # print(a == 8)
    # print('\n')
    # print(Matrix.sum(a, b))
    # print('\n')
    # print(a @ b)
    j = Matrix.read_csv('matrix.csv')

    # print(j)
    # j.write_csv('matrix2.csv')

    print(timeit.timeit(lambda: Matrix.read_csv('matrix.csv'), number=1) * 1_000_000)


if __name__ == '__main__':
    main()
