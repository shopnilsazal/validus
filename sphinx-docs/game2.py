from validus.contract import ValidusBase
from validus.contract import set_validated_contracts
set_validated_contracts(__name__)
import sys
sys.tracebacklimit=None  # Convenience

dx: positive_integer

class Player(ValidusBase):
    name: nonempty_ascii
    x: integer
    y: integer

    def left(self,dx):
        self.x -= dx

    def right(self,dx):
        self.x += dx


if __name__ == "__main__":
    # Show that it works
    name='Guido'; x=0; y=0
    print(f"Instantiating class with name={name}, x={x}, y={y}")
    g=Player(name,x,y)
    dx=1
    print(f"Move to the left with dx={dx}")
    g.left(dx)

    # Show that it is broken
    dx=-1
    print(f"Move to the left with dx={dx}")
    g.left(dx)
