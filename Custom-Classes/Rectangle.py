class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        self._index = 0  # Tracks iteration state

    def __iter__(self):
        self._index = 0  # Reset iteration on each new loop
        return self

    def __next__(self):
        if self._index == 0:
            self._index += 1
            return {'length': self.length}
        elif self._index == 1:
            self._index += 1
            return {'width': self.width}
        else:
            raise StopIteration()

    def __str__(self):
        return f"Rectangle(length={self.length}, width={self.width})"

# Example Usage
if __name__ == "__main__":
    rect = Rectangle(5, 10)
    
    print("Rectangle Details:")
    print(rect)  # Prints a clean string representation
    
    print("\nIterating over the rectangle:")
    for item in rect:
        print(item)  # Prints {'length': 5} followed by {'width': 10}