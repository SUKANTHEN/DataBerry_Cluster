from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from html_remover import cleanhtml
########################################
"""
Function to remove built-in stopwords
"""
def built_in_stopwords_removal(data):
    #data = data.lower()
    words = word_tokenize(data)
    cleandata = (" ").join([word for word in words if not word.lower() in stopwords.words("english")])
    return cleandata
########################################
"""
Function to remove custom defined stopwords
"""
def user_defined_stopwords_removal(data,stopwords_list):
    #data = data.lower()
    words = word_tokenize(data)
    cleandata = (" ").join([word for word in words if not word.lower() in stopwords_list])
    return cleandata
########################################
def auto_datacleaner(data,remove_stopwords=False,stopwords_list=None,remove_html=False):
    print(remove_stopwords,remove_html,stopwords_list)
    if str(remove_html) == "True":
        data = cleanhtml(data)
    if str(remove_stopwords) == "True":
        if str(stopwords_list) != "None":
            if type(stopwords_list) == list:
                cleandata = user_defined_stopwords_removal(data,stopwords_list)
            else:
                return "Enter Words to remove in list/arrays"
        elif str(stopwords_list) == "None":
            cleandata = built_in_stopwords_removal(data)
    else:
        cleandata = data
    return cleandata
