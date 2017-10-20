# attrs-style automatic setting of members with validation
from validus.contract import ValidusBase
import sys
sys.tracebacklimit=None  # Convenience

class Player(ValidusBase):
    name: nonempty_ascii
    x: integer
    y: integer

    def left(self,dx: positive_integer):
        self.x -= dx

    def right(self,dx: positive_integer):
        self.x += dx


if __name__ == "__main__":
    # Show failure
    #name=''; x=0; y=0
    #print(f"Instantiating class with name={name}, x={x}, y={y}")
    #g=Player(name,x,y)

    # Show success
    name='Guido'; x=0; y=0
    print(f"Instantiating class with name={name}, x={x}, y={y}")
    g=Player(name,x,y)
    dx=1
    print(f"Move to the left with dx={dx}")
    g.left(dx)

    # Show failure
    dx=-1
    print(f"Move to the left with dx={dx}")
    g.left(dx)
