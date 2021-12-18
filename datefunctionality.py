import datefinder
from datetime import datetime
from nltk.tokenize import word_tokenize
from utility_functions import set_list_convertor,unique
########### Date validator ##################
def dates_validator(dates,format):
    res = True
    try:
        res = bool(datetime.strptime(dates,format))
    except ValueError:
        res = False
    return res
############### D-M-Y format finder ###############
def valid_dates_identifier(date):
    new_date = ""
    date = str(date).replace('/','-')
    if dates_validator(date,"%d-%m-%Y") == True:
        new_date = datetime.strptime(date,'%d-%m-%Y').strftime('%Y-%m-%d')
    return new_date
#######################################################
def date_validation(text):
  lst = []
  words = word_tokenize(text)
  words = [i for i in words if len(i)>=8]
  for word in words:
    validator = valid_dates_identifier(word)
    if (validator != "") and (validator not in lst):
      lst.append(validator)
  return lst
######################################################
def date_finder(text):
  lst = []
  matches = datefinder.find_dates(text)
  for match in matches:
    lst.append((str(match).split()[0]))
  if len(lst) == 0:
    lst = []
  return lst
#######################################################
def combined_date_extraction(text):
    a1 = date_validation(text)
    a2 = date_finder(text)
    dates = set(a1+a2)
    dates = set_list_convertor(dates)
    dates = ",".join(dates)
    return dates