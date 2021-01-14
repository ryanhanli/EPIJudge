from test_framework import generic_test


def multiply(x: int, y: int) -> int:
    def add(a,b):
        while b:
            carry = a&b
            a,b = a^b, carry<<1
        return a

    product = 0
    while x:
        if x&1:
            product = add(product,y)
        x>>=1
        y<<=1
    return product


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
