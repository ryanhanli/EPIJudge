from test_framework import generic_test


def closest_int_same_bit_count(x: int) -> int:
    for i in range(0,63):
        if((x>>i)&1)!=((x>>i+1)&1):
            return x^((1<<i)|(1<<i+1))
    raise ValueError('All bits are 0 or 1')

    # BETTER ANSWER
    # O(1) space and time complexity
    # Invert the whole x to grab lowest set 0 bit which is turned into a 1 here
    xi_mask = (1 << 64) - 1
    xi = x ^ xi_mask
    xi_lz = xi & ~(xi - 1)
    if xi_lz >> 1 & x:
        return x ^ (xi_lz | xi_lz >> 1)
    elif xi_lz << 1 & x:
        return x ^ (xi_lz | xi_lz << 1)
    else:
        x_lz = (x & ~(x - 1))
        return x ^ (x_lz | x_lz >> 1)



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
