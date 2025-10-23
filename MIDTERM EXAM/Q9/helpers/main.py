# main.py

# Import using aliases
import helpers.string_utils as su
import helpers.math_utils as mu

# Direct import from modules
from helpers.string_utils import shout
from helpers.math_utils import area

if __name__ == "__main__":
    text = "hello world"
    print(su.shout(text))       # Using alias
    print(shout(text))          # Direct import

    l, w = 5, 3
    print(mu.area(l, w))        # Using alias
    print(area(l, w))           # Direct import
