"""This one taught me the gradient is taken with respect to the first parameter
of the function.  I bet that's written down somewhere in Tangent's documentation
and I just overlooked it."""

import random
import tangent


def easy_quadratic(x, y):
    """f(x, y) = x^2 + y^2"""
    return (x * x) + (y * y)


def bigger_polynomial(x, y):
    return (x ** 2) + (x * y) + 0.5 * (y ** 2)
2

def main():
    # By running this, I've "discovered" that the gradient is always calculated
    # with respect to the first argument of the function.
    d_easy = tangent.grad(easy_quadratic, verbose=1)
    # I'd expect, then, that the gradient is always just d/dx{x^2} = 2x,
    # regardless of y's value.  Let's try a collection of random values and
    # check:
    all_good = True
    for _ in range(10):
        xi = 10*random.random() - 5
        yi = 10*random.random() - 5
        all_good &= (d_easy(xi, yi) ==  2*xi)
    if all_good:
        print "The 'easy' derivative function always returns 2*x"
    else:
        print "YIKES!!! Something went wrong!!"

    # There can still be a dependence on the other parameter, though:
    d_big = tangent.grad(bigger_polynomial, verbose=1)
    all_good = True
    for _ in range(10):
        xi = 10*random.random() - 5
        yi = 10*random.random() - 5
        all_good &= (d_big(xi, yi) ==  (2*xi + yi))
    if all_good:
        print "The 'bigger' derivative function always returns 2*x + y"
    else:
        print "DAAAANG something went wrong with d_big"



if __name__ == "__main__":
    main()
