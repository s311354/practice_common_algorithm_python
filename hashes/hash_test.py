import string
import scipy
import random
import matplotlib.pyplot as plt


def polyhash_prime(words, a, prime, m):
    hash = 0
    for word in words:
        hash = (hash * a + ord(word) % prime)

    return abs(hash % m)


def polyhash_noprime(words, a, m):
    """docstring for polyhash_noprime"""
    hash = 0
    for word in words:
        hash = (hash * a + ord(word))

    return abs(hash % m)


def show_distribution(buckets, title):
    """docstring for show_distribution"""
    counts = {}
    for item in buckets:
        if item in counts.keys():
            counts[item] += 1
        else:
            counts[item] = 1

    plt.bar(counts.keys(), counts.values())
    plt.title(title)
    plt.xlabel("Bucket size")
    plt.ylabel("Buckets")
    plt.show()


def randomhash(num):
    """docstring for randomhash"""
    random.seed()
    return random.randint(0, num - 1)


def load_words():
    """docstring for load_words"""
    # hash table
    words = {}
    exclude = set(string.punctuation + "\n")
    word_count = 0

    with open("tale-of-two-cities.txt", "r") as content:
        for line in content:
            line = line.replace("--", ' ')
            line_words = line.split(" ")
            for word in line_words:
                word = ''.join(ch for ch in word if ch not in exclude)

#                 print(word)
                if word:
                    word = word.lower()
                    word_count += 1
                    if word in words:
                        words[word] += 1
                    else:
                        words[word] = 1

    return words


def is_prime(num):
    """docstring for is_prime"""
    """
    d_max = scipy.sqrt(n)
    
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    d = 3

    while n % d != 0 and d <= d_max:
        d += 2

    return d > d_max
    """
    if num == 2:
        return True
    else:
        for i in range(2, num+1):
            if num % i == 0:
                return False
            else:
                return True


def first_prime_greater_than(min):
    """docstring for first_prime_greater_than"""
    for n in scipy.arange(min + 1, min * 2):
        if is_prime(n):
            return n


def main():
    """docstring for main"""
    words = load_words()
    word_count = len(words)
#     print(words)
#     print(word_count)

    # hash table will be at load = 0.5
    m = int(word_count/2)

    # random
    buckets = [0] * m

    for word in words:
        hash = randomhash(m)
        buckets[hash] += 1

    show_distribution(buckets, "Bucket size distribution - Random insert")

    #  polyhash
    prime = first_prime_greater_than(word_count)

    buckets = [0]*m
    for word in words:
        hash = polyhash_prime(word, 31, prime, m)
        buckets[hash] += 1

    show_distribution(buckets, "Bucket size distribution - PolyHash with prime")

    # polyhash, without prime
    buckets = [0]*m
    for word in words:
        hash = polyhash_noprime(word, 31, m)
        buckets[hash] += 1

    show_distribution(buckets, "Bucket size distribution - PolyHash without prime")


if __name__ == '__main__':
    main()
