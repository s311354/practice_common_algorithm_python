
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
    for x in range(0, 20):
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








if __name__ == "__main__":
    main()
