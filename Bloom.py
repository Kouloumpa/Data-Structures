import math
import mmh3
from bitarray import bitarray


class BloomFilter(object):

    def __init__(self, items_count, fp_prob):
        # pithanotita na epistrafei true eno den uparxei h lexi
        self.fp_prob = fp_prob
        # megethos bloom array
        self.size = self.get_size(items_count, fp_prob)
        # arithmos hash functions pou xrhsimopoioume
        self.hash_count = self.get_hash_count(self.size, items_count)
        # dhmiourgeia bloom array
        self.bit_array = bitarray(self.size)
        self.bit_array.setall(0)

    # sinarthsh prosthikhs lexhs sto bloom array
    def add(self, item):

        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            self.bit_array[digest] = True

    # sinarthsh elenxou yparxhs lexhs
    def check(self, item):

        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            if self.bit_array[digest] == False:
                return False
        return True

    @classmethod
    def get_size(self, n, p):
        # n : number of items to be expected
        # p : false positive probability in decimal
        # m  : size of bit array
        m = -(n * math.log(p)) / (math.log(2) ** 2)
        return int(m)

    @classmethod
    def get_hash_count(self, m, n):
        # k : number of hash functions to use
        k = (m / n) * math.log(2)
        return int(k)
