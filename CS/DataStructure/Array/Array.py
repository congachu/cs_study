class Array:
    def __init__(self, size):
        self.data = [None] * size

    def get(self, index):
        if self.checkOutOfRange(index):
            raise IndexError()
        return self.data[index]
    
    def set(self, index, value):
        if self.checkOutOfRange(index):
            raise IndexError()
        self.data[index] = value
        return True

    def checkOutOfRange(self, index):
        return self.len() <= index or 0 > index
    
    def len(self):
        return len(self.data)