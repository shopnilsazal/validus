# First contract design pattern: Django-style
import validus
import sys
sys.tracebacklimit=None  # Convenience

class Player:

    def __init__(self, name, x, y):
        assert validus.isnonempty(name) and validus.isascii(name), 'Player requires a nonempty ascii for name'
        assert validus.isint(str(x)), 'Player requires a integer for x'
        assert validus.isint(str(y)), 'Player requires a integer for y'
        self.name = nonempty_ascii()
        self.x = integer()
        self.y = integer()

    def left(self,dx):
        assert validus.isint(str(dx)) and validus.ispositive(str(dx)), 'Moving left requires a positive number for dx'
        self.x -= dx

    def right(self,dx):
        assert validus.isint(str(dx)) and validus.ispositive(str(dx)), 'Moving right requires a positive number for dx'
        dx = positive_integer()
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
