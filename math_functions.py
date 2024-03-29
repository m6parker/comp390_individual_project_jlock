"""this module contains useful math funcitons to create an encryption. """


# https://rosettacode.org/wiki/Modular_inverse#Python
def extended_gcd(aa, bb):
    """this function uses a while loop to create the encryption. The divmod()
    method takes two numbers as arguments and returns their quotient and remainder in a tuple."""
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient * x, x
        y, lasty = lasty - quotient * y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)


# https://rosettacode.org/wiki/Modular_inverse#Python
def modinv(a, m):
    """this function passes the vaiables to the extended_gcd() funciton and
    checks if g is 1, if it is, return x mod m, if not, raise an error"""
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m
