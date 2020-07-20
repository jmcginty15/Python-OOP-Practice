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

    def __init__(self, start):
        """Create initial serial number with user-defined start value"""
        self.start = start
        self.next = start
    
    def __repr__(self):
        return f'<SerialGenerator start={self.start} next={self.next}>'
    
    def generate(self):
        """Generate the next serial number"""
        next_serial = self.next
        self.next += 1
        return next_serial
    
    def reset(self):
        """Reset the next serial number to the initial start value"""
        self.next = self.start
