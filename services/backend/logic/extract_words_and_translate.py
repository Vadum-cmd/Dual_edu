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

def search_phrasal(lst: List):
    phrasal = set()
    for i in range(len(lst) - 2):
        together = lst[i] + " " + lst[i+1]
        separated = lst[i] + " " + lst[i+2]
        if together in test_phrasal:
            phrasal.add(together)
        if separated in test_phrasal:
            phrasal.add(separated)
    return phrasal

def translate_word(word):
    return translate_text(query_text=word, translator="google", from_language="en", to_language="uk")

