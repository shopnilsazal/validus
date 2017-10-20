# Method using type annotations and decorators
from validus.contract import set_validated_contracts
set_validated_contracts(__name__)
import sys
sys.tracebacklimit=None  # Convenience

@checked
def gcd(a:positive_integer,b:positive_integer):
    """
    Compute greatest common denominator
    """
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    # Show that it works
    a=27; b=36
    print(f"The greatest common denominator of {a} and {b} is:")
    print(gcd(a,b))

    # Show that it is broken
    a=2.7; b=3.6
    print(f"The greatest common denominator of {a} and {b} is:")
    print(gcd(a,b))
