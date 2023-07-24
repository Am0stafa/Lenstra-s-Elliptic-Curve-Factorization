# Lenstra's Elliptic-Curve Factorization in Python

This code implements Lenstra's elliptic curve factorization algorithm in Python. The algorithm attempts to find a non-trivial factor of a given composite number. If it is unable to find a factor within a set number of iterations, the script falls back to using the factorint function from sympy's ntheory module. The combination of Lenstra's algorithm and the sympy fallback provides a robust factorization tool.

A detailed explanation of the algorithm can be found [here](https://en.wikipedia.org/wiki/Lenstra_elliptic-curve_factorization).
also, see [this](https://www.youtube.com/watch?v=V0rDc0V1g5c) video for a good explanation of the algorithm.


## Algorithm Explanation
The Lenstra elliptic curve factorization method leverages the mathematical properties of elliptic curve groups to factor integers. Unlike more standard factorization techniques, Lenstra's approach uses probability to find prime factors.

The core idea is to randomly generate an elliptic curve and a point P on that curve. The order of P is calculated, which will reveal a factor of the target composite number with some probability. This process of generating random curves repeat until a non-trivial factor is uncovered.

The advantage of Lenstra's algorithm is its ability to efficiently find relatively small factors, making it well-suited for factoring large semi-prime numbers. By harnessing the structure of elliptic curve groups, it takes a novel probabilistic approach to integer factorization. \n
Here's a rough sketch of how the algorithm works:

1. Choose a random elliptic curve over the integers modulo n (the number to be factored) and a random point on that curve.

2. Perform a certain number of group operations on the point (i.e., add the point to itself repeatedly). This is equivalent to multiplying the point by a large number.

3. At each step, compute the greatest common divisor (GCD) of n and a certain quantity derived from the point's coordinates. If this GCD is a nontrivial factor of n, then we're done.

4. If no factor is found after a certain number of iterations, go back to step 1 with a new random curve and point.

The idea is that the group operation might "break" if n is composite, leading to a nontrivial GCD.

## Prerequisites

This project requires Python 3.6 or above, as well as the gmpy2 and sympy libraries. You can install these libraries using pip:

```bash
pip install gmpy2 sympy
```

## Usage
To use the script, you need to provide the composite number you want to factor as a command line argument. Here's an example:
```bash
python3 lenstra.py -n 561
```
In this example, 561 is the number we want to factor. The script will then run Lenstra's algorithm with a certain number of iterations to try to find a nontrivial factor. If it can't find one, it will use sympy's factorint function as a fallback.

## Disclaimer
This script is intended for educational purposes only. Please do not use it for malicious or illegal activities.

