import random
import argparse
from gmpy2 import mpz, gcd, invert, isqrt, powmod
from sympy.ntheory import factorint

def mod_inv(a, n):
    return int(invert(mpz(a), mpz(n)))

def elliptic_add(p, q, a, n):
    xp, yp, zp = p
    xq, yq, zq = q
    if (xp, yp, zp) == (0,1,0):
        return q
    if (xq, yq, zq) == (0,1,0):
        return p
    u = (yq - yp) % n
    v = (xq - xp) % n
    u2 = powmod(u, 2, n)
    v2 = powmod(v, 2, n)
    v3 = powmod(v, 3, n)
    x = (u2 - v2 - 2*v*xp) % n
    y = (u*(v2 - x) - v3*yp) % n
    z = (v3*zp) % n
    return x, y, z

def elliptic_double(p, a, n):
    xp, yp, zp = p
    u = (3*xp**2 + a*zp**2) % n
    v = 2*yp*zp % n
    u2 = powmod(u, 2, n)
    v2 = powmod(v, 2, n)
    v3 = powmod(v, 3, n)
    x = (u2 - 2*v*xp) % n
    y = (u*(v*xp - x) - v3*yp) % n
    z = (v3*zp) % n
    return x, y, z

def lenstra(n, limit):
    g = n
    while g == n:
        q = (random.randint(0, n-1), random.randint(0, n-1), random.randint(1, n-1))
        a = random.randint(0, n-1)
        for _ in range(limit):
            q = elliptic_double(q, a, n)
            g = gcd(q[2], n)
            if 1 < g < n:
                return g
    return None

def main():
    parser = argparse.ArgumentParser(description='Factor a number using Lenstra\'s Elliptic-Curve Factorization.')
    parser.add_argument('-n', '--number', type=int, required=True, help='The composite number to factor.')
    args = parser.parse_args()

    n = args.number
    limit = 500000  

    factor = lenstra(n, limit)
    if factor is not None:
        print(f"Found a factor of {n} using Lenstra's algorithm.")
        print(f"The factor is {factor}")
        print(f"The other factor is {n // factor}")
    else:
        print(f"Failed to find a factor of {n} using Lenstra's algorithm.")
        print(f"Trying to factor {n} using sympy's factorint function.")
        factors = factorint(n)
        print(f"Factors of {n} are {factors}")

if __name__ == '__main__':
    main()
