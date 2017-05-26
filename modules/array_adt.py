import ctypes

class Array(object):
    """
    Creates an array with size elements.
    :param size: size of array.
    """
    def __init__(self, size):
        """
        Creates an array with the given size

        :param size: size of the array
        """
        #assert size > 0, "Array size must be > 0"
        self._size = size
        array = ctypes.py_object * size  # creates an array with ctypes library and py_object
        self._elements = array()  # sets the newly created array to the attribute _items
        self.clear(None)  # clears the array with setting every item to None

    def __len__(self):
        """
        Returns the size of the array.

        :return: the size of the array
        """
        return self._size

    def __getitem__(self, index):
        """
        Gets the value of the element.

        :param index: the index of element.
        :return: value of the element.
        """
        if not 0 <= index < self._size:
            raise IndexError('Invalid index')
        return self._elements[index]


    def __setitem__(self, index, value):
        """
        Puts the value in the array element at index position.

        :param index: the index element.
        :param value: the value of element.
        """
        if not 0 <= index < self._size:
            raise IndexError('Invalid index')
        self._elements[index] = value


    def clear(self, value):
        """
        Clears the array by setting each element to the given value.

        :param value: the value of element.
        """
        for i in range(len(self)):
            self._elements[i] = value

    def __str__(self):
        """
        Converts the adt structure to a string.
        :return: converted structure.
        """
        to_return = "("
        for index in range(self._size - 1):
            to_print = str(self[index])
            to_return = to_return + to_print + ","
        to_print = str(self[self._size - 1])
        return to_return + to_print + ")"

    def __iter__(self):
        """
        Returns the array's iterator for traversing the elements.

        :return: the array's iterator for traversing the elements.
        """
        return _ArrayIterator(self._elements)

class _ArrayIterator:
    """
    An iterator for the Array ADT.
    """
    def __init__(self, the_array):
        self._array_ref = the_array
        self._cur_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur_index < len(self._array_ref):
            entry = self._array_ref[self._cur_index]
            self._cur_index += 1
            return entry
        else:
            raise StopIteration

class Array2D(object):
    """
        Implementation of the Array2D ADT using an array of arrays.
        """

    def __init__(self, num_rows, num_cols):
        """
        Creates a 2D array of size num_rows x num_cols.
        :param num_rows: number of rows.
        :param num_cols: number of columns.
        """

        # Creates a 1D array to store an array reference for each row.
        self.rows = Array(num_rows)

        # Creates the 1D arrays for each row of the 2D array.
        for i in range(num_rows):
            self.rows[i] = Array(num_cols)

    def num_rows(self):
        """
        Returns the number of rows in the 2D array.

        :return:
        """
        return len(self.rows)

    def num_cols(self):
        """
        Returns the number of columns in the 2D array.

        :return: the number of columns in the 2D array.
        """
        return len(self.rows[0])
    def clear(self, value):
        """
        Clears the array by setting every element to the given value.

        :param value: value to be set.
        """
        for row in self.rows:
            row.clear(value)

    def __getitem__(self, index_tuple):
        """
        Gets the contents of the element at position [i, j]

        :param index_tuple: the index of position.
        :return: the value.
        """
        assert len(index_tuple) == 2, "Invalid number of array subscripts."
        row = index_tuple[0]
        col = index_tuple[1]
        if not (0 <= row < self.num_rows() and 0 <= col < self.num_cols()):
            raise IndexError('Invalid index')
        array_1d = self.rows[row]
        return array_1d[col]

    def __setitem__(self, index_tuple, value):
        """
        Sets the contents of the element at position [i,j] to value.

        :param index_tuple: the index of position.
        :param value: the value to be set.
        """
        assert len(index_tuple) == 2, "Invalid number of array subscripts."
        row = index_tuple[0]
        col = index_tuple[1]
        if not (0 <= row < self.num_rows() and 0 <= col < self.num_cols()):
            raise IndexError('Invalid index')
        array_1d = self.rows[row]
        array_1d[col] = value

    def __str__(self):
        """
        For print() function.
        :return: string to print
        """
        string = "\n"
        for i in range(0, self.num_rows()):
            for j in range(0, self.num_cols()):
                string += str(self[(i, j)]) + " "
            string += "\n"
        return string[1:-1]