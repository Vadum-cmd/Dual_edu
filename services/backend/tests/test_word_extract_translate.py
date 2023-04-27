from logic.extract_words_and_translate import *


def test_extract_text_from_pdf():
    assert extract_text_from_pdf('test_books/test_file1.pdf') == "Once upon a time  "
    assert extract_text_from_pdf('test_books/test_file2.pdf') == "ThErE Se emEd tO Be a Story!  "
    assert extract_text_from_pdf('test_books/test_file3.pdf') == "AND IT ’S QUITE UNIQUE ? "
    assert extract_text_from_pdf('test_books/test_file4.pdf') == " "


def test_word_tokenization():
    assert word_tokenization("i really love pancakes") == ['i', 'really', 'love', 'pancakes']
    assert word_tokenization(",,,...my ,,.,.man? be!!@ you???// okay") == ['my', 'man', 'be', 'you', 'okay']
    assert word_tokenization("Jeorge Hannah I General") == ['jeorge', 'hannah', 'i', 'general']
    assert word_tokenization("nO, Like, sErioUsly") == ['no', 'like', 'seriously']
    assert word_tokenization("arrived, granted, making") == ['arrive', 'grant', 'make']
    assert word_tokenization("am, is, are, him") == ['be', 'be', 'be', 'him']


def test_search_phrasal():
    assert search_phrasal(['well', 'i', 'will', 'head', 'off']) == set()
    assert search_phrasal(['how', 'about', 'we', 'head', 'off', 'right', 'this', 'moment']) == {'head off'}
    assert search_phrasal(['turn', 'he', 'on', 'right', 'this', 'moment']) == {'turn on'}
    assert search_phrasal(['come', 'in', 'for', 'right', 'this', 'moment']) == {'come in', 'come in for'}
