from enum import auto
import uuid
import re
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from nltk import data
from werkzeug.utils import secure_filename
from googletrans import Translator
from googletranslater import google_translator
from text_quality import word_counter,query_length_finder
from phi_extractor import charnum_replacer,phone_number_detector,email_detector,gender_identifier
from datefunctionality import combined_date_extraction
from flask_restful import Resource,Api
from flask_httpauth import HTTPBasicAuth
from flask import jsonify
from stopwords_remover import auto_datacleaner
from toxic_words import toxic_words_identifier,toxic_word_replacer
from catboost import CatBoostClassifier, Pool
from validation_identifiables import keys_for_validation,Document_Number_validator

app = Flask(__name__)
auth = HTTPBasicAuth()
translator = Translator()
###############################################
DataberryML = CatBoostClassifier()           
DataberryML.load_model('models/catmodel.cbm')
###############################################
#---------- Basic Auth ---------#

#------------- Home Page --------------#
@app.route('/',methods=['GET', 'POST'])
def index():
    return render_template("index.html")
    #return 'Welcome to DataBerry Cluster API'

#------------- Create Auth Tokens Page --------------#
@app.route('/home.html',methods=['GET', 'POST'])
def home_page():
    return render_template("home.html")

#------------- 404 HTML Page  --------------#
@app.route('/404.html',methods=['GET', 'POST'])
def error_page():
    return render_template("404.html")

#------------- Create Auth Tokens Page --------------#
@app.route('/login.html',methods=['GET', 'POST'])
def login_page():
    return render_template("login.html")

#------------- Thanks Page --------------#
@app.route('/thanks.html',methods=['GET', 'POST'])
def thanks_page():
    return render_template("thanks.html")

#----------- Text Quality End-point --------------#
@app.route('/text_quality', methods=['POST'])
#@auth.login_required
def legality_checker():
    if request.method == 'POST':
        request_data = request.get_json()
        text = request_data['text']
        lang = google_translator(text)
        all_words,len_all_words = word_counter(text)
        clean_text,len_clean_text = query_length_finder(text) # Spaces removed
        toxicity = toxic_words_identifier(text)
        all_words = set(all_words)
        data = {"language":lang,"count_of_words":len_all_words,"count_unique_words":len(all_words),"query_length":len_clean_text,"toxicity":toxicity}
        data = jsonify(data)
    return data

#----------- Personal Identifier End-point --------------#
@app.route('/personal_identifier', methods=['POST'])
#@auth.login_required
def personal_identifier():
    if request.method == 'POST':
        request_data = request.get_json()
        text = request_data['text']
        text = charnum_replacer(text)
        nums = phone_number_detector(text)
        emails = email_detector(text)
        gender = gender_identifier(text)
        dates = combined_date_extraction(text)
        data = {"dates":dates,"phone_number":nums,"email":emails,"gender":gender}
        data = jsonify(data)
    return data

#----------- Translator ----------#
@app.route('/translate', methods=['POST'])
def translator():
    if request.method == 'POST':
        try:
            request_data = request.get_json()
            text_to_translate = request_data["text"]
            selected_language = request_data["output_language"]
            translated_text = translator.translate(str(text_to_translate),dest=selected_language)
            print(translated_text)
            text = translated_text.text
            pronunciation_data = translated_text.pronunciation
            if (str(pronunciation_data) == "None"):
                pronunciation_data = "{Sorry, data not available}"
            confidence = round((translator.translate(text_to_translate, dest=selected_language).extra_data["confidence"])*100, 2)
        except:
            pronunciation_data = "-"
            text = "{ERROR: We are not able to handle your request right now}"
            confidence = "-"
        data = {"translated_text":text,"pronunciation":pronunciation_data}
        data = jsonify(data)
    return data

#----- Auto Data Cleaner ----#
@app.route('/datacleaner', methods=['POST'])
#@auth.login_required
def data_cleaner():
    if request.method == 'POST':
        request_data = request.get_json()
        text = request_data['text']
        remove_html = request_data['remove_html']
        remove_sw = request_data["remove_stopwords"]
        stopwords = request_data["stopwords_list"]
        x = auto_datacleaner(text,remove_html=remove_html,remove_stopwords=remove_sw,stopwords_list=stopwords)
        data = {"cleaned_text":x}
        data = jsonify(data)
    return data

#----- Detoxifier API ----#
@app.route('/detoxify', methods=['POST'])
#@auth.login_required
def detoxifier():
    if request.method == 'POST':
        request_data = request.get_json()
        text = request_data['text']
        x = toxic_word_replacer(text)
        data = {"cleaned_text":x}
        data = jsonify(data)
    return data

@app.route('/gibberish_check', methods=['POST'])
#@auth.login_required
def gibberish_check():
    if request.method == 'POST':
        request_data = request.get_json()
        text = request_data['text']
        pred = DataberryML.predict([text])
        data = {"gibberish_data":int(pred)}
        data = jsonify(data)
    return data

@app.route('/e-validator', methods=['POST'])
#@auth.login_required
def validation_check():
    if request.method == 'POST':
        request_data = request.get_json()
        text = request_data['data']
        check_type = request_data['type_data']
        if check_type in keys_for_validation:
            regex_check_type = keys_for_validation[check_type]
            validID = Document_Number_validator(regex_check_type,text)
            data = {"validID":validID}
            data = jsonify(data)
        else:
            val = ",".join(keys_for_validation)
            data = f"Invalid Personal Identifier. We currently support {val} only"
    return data

if __name__ == '__main__':
    app.run(debug=True,host = '0.0.0.0',port=8080)