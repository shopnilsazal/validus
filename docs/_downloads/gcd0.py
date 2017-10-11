# Method 0: Traditional method
import validus
import sys
sys.tracebacklimit=None  # Convenience

def gcd(a,b):
    """
    Compute greatest common denominator
    """
    assert validus.isint(str(a)) and validus.ispositive(str(a)), 'gcd requires a positive number for a'
    assert validus.isint(str(b)) and validus.ispositive(str(b)), 'gcd requires a positive number for b'

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
