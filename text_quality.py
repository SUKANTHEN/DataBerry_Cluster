import re
import nltk
from nltk.tokenize import word_tokenize

def query_length_finder(text):
    clean_text = " ".join(text.split())
    length_text = len(clean_text)
    return clean_text,length_text

def word_counter(text):
    all_words = word_tokenize(text)
    len_all_words = len(all_words)
    return all_words,len_all_words