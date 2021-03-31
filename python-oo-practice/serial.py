"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        "Create a starting number to count from and a counter to keep track of  times called"
        self.start = self.current_num = start
        self.count = -1

    def generate(self):
        "return strting number first time called and increment after"
        self.count += 1
        if self.count == 0:
            return self.current_num
        else:
            self.current_num += 1
            return self.current_num

    def __repr__(self):
        "Show reprenstation"
        return f"<start={self.start} current_num={self.current_num}>"

    def reset(self):
        "reset start number and count to orginal value"
        self.count = -1
        self.current_num = self.start
