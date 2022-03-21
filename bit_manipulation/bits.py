
def swap_ints(a, b):
    """docstring for swap_ints"""
    a ^= b
    b ^= a
    a ^= b
    return [a, b]


def myabs(x):
    """docstring for myabs"""
    # Two's complement conversion from negative to positive
    high_bit_mask = x >> 31
    return (x ^ high_bit_mask) - high_bit_mask

def modulo(a, b):
    """docstring for modulo"""
    mask = ( (1 << b) - 1 )
    return a & mask


def next_power_of_2(x):
    """docstring for next_power_of_2"""
    x -= 1
    x |= x >> 1
    x |= x >> 2
    x |= x >> 4
    x |= x >> 8
    x |= x >> 16
    x += 1
    return x


def has_parity_parallel(x):
    """docstring for has_parity_parallel"""
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x  &= 0xf
    return ( 0x6996 >> x) & 1


# has odd number of bits
def has_parity(x):
    """docstring for has_parity"""
    parity = False

    while x:
        parity = not parity
        x &= (x - 1)

    return parity


def get_sign(x):
    """docstring for get_sign"""
    return -(x < 0)


def add(a, b):
    """docstring for add"""
    while a:
        carry = b&a
        b ^= a # Sum of bits of a and b where at least one of the bits is not set
#         print(carry << 1)
        a = carry << 1 # Carry is shifted by one so that adding it to b gives the required sum
    return b


def rotate_left(x, n):
    """docstring for rotate_left"""
    # assumes a 32 bit word size
    rotated_left = x >> (-n & 31)
#     print(rotated_left)
    return ( x << n | rotated_left)


def clear_bit(x, position):
    """docstring for clear_bit"""
    return x & ~(1 < position)


def set_bit(x , position):
    """docstring for set_bit"""
    return x | (1 << position)


def toggle_bit(x, position):
    return x ^ (1 << position)


def get_bits(x, pos, n):
    """docstring for get_bits"""
#     print (~( ~0 << n))
    mask = ~(~0 << n)
    return ( x >> (pos + 1 - n) & mask)


def is_power_of_2(x):
    """docstring for is_power_of_2"""
    return (x & x - 1) == 0


def is_even(x):
    """docstring for is_even"""
    return x & 1 == 0


def hanming_distance(x, y):
    """TODO: Docstring for hanming_distance."""

    difference = x ^ y
    count = 0
    while difference:
        # print(bin(difference))
        difference &= difference - 1
        count += 1

    return count


def is_bit_set(x, pos):
    """TODO: Docstring for is_bit_set.

    :function: TODO
    :returns: TODO

    """
    return(x & (1 << pos)) != 0


def hanming_weight(x):
    """docstring for hanming_weight"""
    if x < 0:
        return None

    count = 0
    while x:
        x &= x - 1
        count += 1

    return count


def hacker_pop_count(i):
    """docstring for hacker_pop_count: Returns the number of 1 bit in the value of i"""
    """ hacker_popcnt """
    i -= ((i >> 1) & 0x55555555)
    i = (i & 0x33333333) + ((i >> 2 ) & 0x33333333)

    return (((i + (i >> 4) & 0xF0F0F0F) * 0x1010101) & 0xFFFFFFFF) >> 24


def main():
    """docstring for main"""
    for x in range(0, 32):
        print(x, bin(x), hex(x))

    print("Hamming distance: 1010111100 and 1001010101", hanming_distance(0b1010111100, 0b1001010101))

    print("Bit 0: 1011 1100 set?", is_bit_set(0b1010111100, 0))
    print("Bit 1: 1011 1100 set?", is_bit_set(0b1010111100, 1))
    print("Bit 2: 1011 1100 set?", is_bit_set(0b1010111100, 2))

    print("Hamming weight: 1010111100:", hanming_weight(0b1010111100))
    print("Hamming weight: 0b11111111:", hanming_weight(0b11111111))

    print("Hacker PopConut: " + str(bin(1231424)) + ":", hacker_pop_count(1231424))
    print("Hacker PopCount: " + str(bin(1)) + ":", hacker_pop_count(1))
    print("Hacker PopCount: " + str(bin(8568)) + ":", hacker_pop_count(8568))


    for x in range(0, 5):
        print(str(x) + 'is even?', is_even(x))


    for x in range(0, 8):
        print(str(x) + 'is power of 2?', is_power_of_2(x))


    print("Get 3 bits starting at position 5 in 1010111100", bin(get_bits(0b1010111100, 5, 3)))
    print("Get 3 bits starting at position 9 in 1010111100", bin(get_bits(0b1010111100, 9, 3)))

    print("Get 4 bits starting at position 9 in 1010111100", bin(get_bits(0b1010111100, 9, 4)))


    print("Set bit 4 to 0: 01010010", bin(clear_bit(0b01010010, 4)))
    print("Set bit 0 to 1: 01010010", bin(set_bit(0b01010010, 0)))
    print("Toggle bit 1: 01010010", bin(toggle_bit(0b01010010, 1)))

    print("Rotate left 5 positions: 01001000100101011001010010011011:",
          bin(rotate_left(0b01001000100101011001010010011011, 5)))


    print("3 + 5 = ", add(3, 5))
    print("33 + 51 = ", add(33, 51))
    print("40 + 90 = ", add(40, 90))

    print("Sign of 5", get_sign(5))
    print("Sign of 0", get_sign(0))
    print("Sign of -1", get_sign(-1))
    print("Sign of -3", get_sign(-3))

    for x in range(0, 12):
        print("has parity: " + str(x), has_parity(x), bin(x))

    for x in range(0, 7):
        print("has parity (parallel): " + str(x), has_parity_parallel(x), bin(x))


    print("Next power of 2 after 3", next_power_of_2(3))
    print("Next power of 2 after 4", next_power_of_2(4))
    print("Next power of 2 after 45", next_power_of_2(45))

    print("4 mod 2", modulo(4, 2))
    print("5 mod 2", modulo(5, 2))
    print("10 mod 3", modulo(10, 3))

    print("abs -134", myabs(-134))
    print("abs 99", myabs(99))

    print("swap 1, 3", swap_ints(1, 3))
    print("swap 213, 14", swap_ints(213, 14))

if __name__ == "__main__":
    main()
