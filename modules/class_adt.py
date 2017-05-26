from array_adt import Array



class Array_repr(object):
    "Groups all data in 1d array"

    def __init__(self, data):
        self.data = data
        array = Array(len(self.data) + 1)
        array[0] = "Result:"
        for i in range(1,len(array)):
            array[i] = self.data[i-1]
        self.array = array
    def print_res(self):
        "Returns the array"
        for i in range(len(self.array)):
            print (self.array[i])