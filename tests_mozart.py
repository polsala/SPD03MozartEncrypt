# -*- coding: utf-8 -*-
import unittest
from mozart import Mozart


class TestMozart(unittest.TestCase):
    def test_mozart(self):
        ALPHABET_ALL = (
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'ñ', 'Ñ', '-', '+', '.', ';', '{', '}', '(', ')', '“', ',', '”'
        )

        text = """
            “It is our suffering that brings us together. It is not love. Love does not obey the mind, and turns 
            to hate when forced. The bond that binds us is beyond choice. We are brothers. We are brothers in what we 
            share. In pain, which each of us must suffer alone, in hunger, in poverty, in hope, we know our 
            brotherhood. We know it, because we have had to learn it. We know that there is no help for us but 
            from one another, that no hand will save us if we do not reach out our hand. And the hand that you 
            reach out is empty, as mine is. You have nothing. You possess nothing. You own nothing. You are free. 
            All you have is what you are, and what you give.”
            ― Ursula K. Le Guin
            """

        expected_res = ''.join([x for x in text if x in ALPHABET_ALL])

        mozart_obj = Mozart(5, 6, ALPHABET_ALL, 19)

        mozart_obj.encrypt(text, 10)

        res = mozart_obj.decrypt(10)

        self.assertEqual(res, expected_res)
