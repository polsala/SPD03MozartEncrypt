from math import log2, ceil
from itertools import product, chain
from functools import reduce
from PIL import Image
import numpy as np

ALPHABET_ALL = (
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'ñ', 'Ñ', '-', '+', '.', ';', '{', '}', '(', ')', ':', '[', ']'
)


class Mozart(object):
    def __init__(self, index_start, index_jumps, alphabet=ALPHABET_ALL, binary_len_key=None):
        """
        :param binary_len_key n will be len of binary expression in truth table
        (minimum input number is log2(n) upper round: default)
        :param alphabet: iterable of chars
        :param key: iterable of chars
        """

        self.aphabet_len = len(alphabet)
        self.alphabet = alphabet

        if not binary_len_key:
            self.binary_len_key = ceil(log2(self.aphabet_len))  # 2^n -> upper round n  | 3.1 = 4
        else:
            if binary_len_key < ceil(log2(self.aphabet_len)):
                raise ValueError('binary_len_key: minimum input number is log2(n) upper round where n is alphabet len')
            else:
                self.binary_len_key = int(binary_len_key)
        self.binary_fake_assign = self.create_fake_binary_assign(alphabet, self.binary_len_key, index_start, index_jumps)
        self.rgb_mapping = {}
        for i, v in self.binary_fake_assign.items():
            self.rgb_mapping[i] = self.binary_to_rgb(v)
        self.reverse_rgb = self.rgb_mapping.__class__(map(reversed, self.rgb_mapping.items()))

    @staticmethod
    def divide_chunks(l, n):
        for i in range(0, len(l), n):
            yield l[i:i + n]

    @staticmethod
    def binary_to_rgb(number):
        B = number % 256
        G = ((number - B) / 256) % 256
        R = ((number - B) / 256 ** 2) - G / 256

        return int(R), int(G), int(B)

    @staticmethod
    def product_index(sorted_list, interesting_pattern):
        result = 0
        for number in interesting_pattern:
            result = result * len(sorted_list) + sorted_list.index(number)
        return result

    @staticmethod
    def create_fake_binary_assign(alphabet, permutation_size, index_start, index_jumps):
        # mod rgb colors
        res = {}
        t_size = pow(2, permutation_size)
        if index_jumps * len(alphabet) + index_start > t_size:
            raise IndexError('Number of jumps invalid')
        truth_table = list(product([0, 1], repeat=permutation_size))
        indx_list = index_start - 1
        for i, k in enumerate(alphabet):
            # Generate a binary number from true table row
            res[k] = reduce(lambda a, b: (a << 1) + int(b), truth_table[indx_list])
            indx_list += index_jumps

        return res

    def encrypt(self, phrase, split_key):
        pixels = []
        for c in phrase:
            cp = self.rgb_mapping.get(c, None)
            if cp:
                pixels.append(cp)

        pixels = list(self.divide_chunks(pixels, split_key))  # Need quadratic
        # Todo in a future add matrix rotations
        exc = split_key - len(pixels[-1])
        if exc != 0:
            for _ in range(0, exc):
                pixels[-1].append((232, 20, 7))  # Todo change in a future for random

        array = np.array(pixels, dtype=np.uint8)

        new_image = Image.fromarray(array)
        new_image.save('image_01.png')

    def decrypt(self, split_key, image_path='image_01.png'):
        img = Image.open(image_path)
        # pixels = list(chain(chain(np.array(img).tolist())))
        pixels = np.array(img).tolist()
        res = ''
        for l in pixels:
            for rgb in l:
                decoded = self.reverse_rgb.get(tuple(rgb), None)
                if decoded:
                    res += decoded
        return res
