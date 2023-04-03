import PyPDF2
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
from translators import translate_text


nltk.download('wordnet')
test_phrasal = ["ask out", "blow up", "back up"]

def extract_text_from_pdf(file_path: str):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        return text

def word_tokenization(text: str):
    tokenizer = RegexpTokenizer(r'\w+')
    words = tokenizer.tokenize(text)
    words = [word.lower() for word in words if word.isalpha()]
    for i in range(len(words)):
        words[i] = WordNetLemmatizer().lemmatize(words[i], 'v')
    return words

def search_phrasal(lst: list):
    phrasal = set()
    for i in range(len(lst) - 3):
        together = lst[i] + " " + lst[i+1]
        separated = lst[i] + " " + lst[i+2]
        three_words = lst[i] + lst[i+1] + lst[i+2]
        four_words = lst[i] + lst[i+1] + lst[i+2] + lst[i+3]
        if together in test_phrasal:
            phrasal.add(together)
        if separated in test_phrasal:
            phrasal.add(separated)
        if three_words in test_phrasal:
            phrasal.add(three_words)
        if four_words in test_phrasal:
            phrasal.add(four_words)
    return phrasal

def translate_word(word):
    return translate_text(query_text=word, translator="google", from_language="en", to_language="uk")

