import PyPDF2
from nltk.tokenize import RegexpTokenizer
from translators import translate_text

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        return text

def word_tokenization(text):
    tokenizer = RegexpTokenizer(r'\w+')
    words = tokenizer.tokenize(text)
    words = set([word.lower() for word in words if word.isalpha()])
    return words

def translate_word(word):
    return translate_text(query_text=word, from_language="en", to_language="uk")
