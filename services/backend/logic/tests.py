import unittest
from extract_words_and_translate import *

# Run this to start testing: "python -m unittest tests.py"


class TestExtractText(unittest.TestCase):
    def test_regular(self):
        actual = extract_text_from_pdf('test_file1.pdf')
        expected = "Once upon a time  "
        self.assertEqual(actual, expected)

    def test_mixed_case(self):
        actual = extract_text_from_pdf('test_file2.pdf')
        expected = "ThErE Se emEd tO Be a Story!  "
        self.assertEqual(actual, expected)

    def test_caps(self):
        actual = extract_text_from_pdf('test_file3.pdf')
        expected = "AND IT ’S QUITE UNIQUE ? "
        self.assertEqual(actual, expected)

    def test_empty(self):
        actual = extract_text_from_pdf('test_file4.pdf')
        expected = " "
        self.assertEqual(actual, expected)


class TestTokenization(unittest.TestCase):
    def test_regular(self):
        my_text = "i really love pancakes"
        actual = word_tokenization(my_text)
        expected = ['i', 'really', 'love', 'pancakes']
        self.assertEqual(actual, expected)

    def test_punctuation(self):
        my_text = ",,,...my ,,.,.man? be!!@ you???// okay"
        actual = word_tokenization(my_text)
        expected = ['my', 'man', 'be', 'you', 'okay']
        self.assertEqual(actual, expected)

    def test_upper_case(self):
        my_text = "Jeorge Hannah I General"
        actual = word_tokenization(my_text)
        expected = ['jeorge', 'hannah', 'i', 'general']
        self.assertEqual(actual, expected)

    def test_mixed_case(self):
        my_text = "nO, Like, sErioUsly"
        actual = word_tokenization(my_text)
        expected = ['no', 'like', 'seriously']
        self.assertEqual(actual, expected)

    def test_tenses(self):
        my_text = "arrived, granted, making"
        actual = word_tokenization(my_text)
        expected = ['arrive', 'grant', 'make']
        self.assertEqual(actual, expected)

    def test_forms(self):
        my_text = "am, is, are, him"
        actual = word_tokenization(my_text)
        expected = ['be', 'be', 'be', 'him']
        self.assertEqual(actual, expected)


class TestSearchPhrasal(unittest.TestCase):
    def test_phrasal_in_the_end(self):
        my_list = ['well', 'i', 'will', 'head', 'off']
        actual = search_phrasal(my_list)
        expected = set()
        self.assertEqual(actual, expected)

    def test_regular(self):
        my_list = ['how', 'about', 'we', 'head', 'off', 'right', 'this', 'moment']
        actual = search_phrasal(my_list)
        expected = {'head off'}
        self.assertEqual(actual, expected)

    def test_separated(self):
        my_list = ['turn', 'he', 'on', 'right', 'this', 'moment']
        actual = search_phrasal(my_list)
        expected = {'turn on'}
        self.assertEqual(actual, expected)

    def test_three(self):
        my_list = ['come', 'in', 'for', 'right', 'this', 'moment']
        actual = search_phrasal(my_list)
        expected = {'come in', 'come in for'}
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
