"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers."""
    
    def __init__(self, num):
        """Initialize the serial number generator with a starting number."""
        self.start = num
        self.num = num
    
    def generate(self):
        """Increment self by 1 and return."""
        self.num += 1
        return self.num
    
    def reset(self):
        """Reset current num to starting num."""
        self.num = self.start

    def describe(self):
        """Describe what the current serial num is."""
        print(f"The current serial is {self.num}.")
      