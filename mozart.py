from math import log2, ceil
from itertools import product
from functools import reduce

ALPHABET_ALL = (
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'ñ', 'Ñ', '-', '+', '.', ';', '{', '}', '(', ')', ':', '[', ']'
)


class Mozart(object):
    def __init__(self, alphabet=ALPHABET_ALL, binary_len_key=None, key='sdfskkkllaiiiaiuiifnnal238s', permutation_size=None):
        """
        :param binary_len_key n will be len of binary expression in truth table
        (minimum input number is log2(n) upper round: default)
        :param alphabet: iterable of chars
        :param key: iterable of chars
        """

        self.aphabet_len = len(alphabet)
        if not permutation_size:
            self.max_permutations = self.aphabet_len / 2
        else:
            permutation_size = int(abs(permutation_size))
            if permutation_size > self.aphabet_len:
                raise ValueError('permutation_size should can\'t be greater than alphabet size')
            else:
                self.max_permutations = permutation_size
        self.alphabet = alphabet
        self.key = key

        if not binary_len_key:
            self.binary_len_key = ceil(log2(self.aphabet_len))  # 2^n -> upper round n  | 3.1 = 4
        else:
            if binary_len_key < ceil(log2(self.aphabet_len)):
                raise ValueError('binary_len_key: minimum input number is log2(n) upper round where n is alphabet len')
            else:
                self.binary_len_key = int(binary_len_key)
        self.binary_fake_assign = self.create_fake_binary_assign(alphabet, self.binary_len_key)

    @staticmethod
    def binary_to_rgb(binary):
        pass

    @staticmethod
    def create_fake_binary_assign(alphabet, permutation_size):
        # mod rgb colors
        res = {}

        truth_table = list(product([0, 1], repeat=permutation_size))
        # TODO randomize table with key or implement after in rgb compression
        for i, k in enumerate(alphabet):
            # Generate a binary number from true table row
            res[k] = reduce(lambda a, b: (a << 1) + int(b), truth_table[i])

        return res

    def encrypt(self, phrase):
        for i, c in phrase:
            continue
        pass

    def decrypt(self):
        pass
