from test_framework import generic_test


def parity(x: int) -> int:
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 1


# Caching is an option

# Variants
def propagate_right_most_set_bit(x):
    return x | (x - 1)

def mod_power_2(x, power):
    return x & ((1<<power)-1)

if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
