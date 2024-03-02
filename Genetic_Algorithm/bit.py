
import random

class BitListGenerator:
    def __init__(self):
        self.num_lists = 100
        self.list_length = 6

    def generate_bit_list(self):
        """Generate a list of random bits."""
        return [random.randint(0, 1) for _ in range(self.list_length)]

    def generate_bit_lists(self):
        """Generate multiple lists of bits."""
        return [self.generate_bit_list() for _ in range(self.num_lists)]

    def sort_bit_lists(self, bit_lists):
        """Sort a list of lists containing bit lists."""
        return sorted(bit_lists)

    def pick_top_two_lists(self, sorted_bit_lists):
        """Pick the top two lists from a sorted list of lists."""
        return sorted_bit_lists[:2]

# Example usage:
generator = BitListGenerator()

# Generate bit lists
bit_lists = generator.generate_bit_lists()

# Sort the lists
sorted_bit_lists = generator.sort_bit_lists(bit_lists)

# Pick the top two lists
top_two_lists = generator.pick_top_two_lists(sorted_bit_lists)

# Print the top two lists
print("Top two lists:")
for i, bit_list in enumerate(top_two_lists, 1):
    print(f"List {i}: {bit_list}")




