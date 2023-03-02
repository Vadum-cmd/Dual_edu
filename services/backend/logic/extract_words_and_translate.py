import PyPDF2
from nltk.tokenize import RegexpTokenizer


def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        return text

def get_unique_words(text):
    arr = text.split()
    arr = [i.lower() for i in list(set(arr))]
    for i in range(len(arr)):
        for j in range(len(arr[i]) - 1, -1, -1):
            if arr[i][j].isalpha():
                pass
            else:
                if j == len(arr[i]) - 1:
                    arr[i] = arr[i][:j]
                else:
                    arr[i] = arr[i][:j] + arr[i][j + 1:]
    return arr

def word_tokenization(text):
    tokenizer = RegexpTokenizer(r'\w+')
    words = tokenizer.tokenize(text)
    words = [word.lower() for word in words if word.isalpha()]
    return words
