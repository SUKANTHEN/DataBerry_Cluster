import re
from nltk.tokenize import word_tokenize

def set_list_convertor(set):
    return [*set, ]

def email_detector(data):
    email = re.findall('\S+@\S+',data)
    if len(email)>0:
        email = ",".join(email)
    else:
        email = ""
    return email

def phone_number_detector(data):
    length = 8
    x = re.findall('[0-9]+', data)
    nums1 = [i for i in x if len(i)>=length]
    nums2 = re.findall(r'[\+\(]?[0-9][0-9 .\-\(\_\)]{8,}[0-9]',data)
    nums = set(nums1+nums2)
    nums = set_list_convertor(nums)
    if len(nums)>0:
        nums = ",".join(nums)
    else:
        nums = ""
    return nums

units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight","nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
         "sixteen", "seventeen", "eighteen", "nineteen","twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def charnum_replacer(text):
    text = text.lower()
    for i in units:
        text = text.replace(i,"101")
    return text

def gender_identifier(data):
    headers = ['female','male','f','m','man','woman','women','men','lgbt','transgender','shemale','bisexual','gay','lesbian']
    x = data.lower()
    x = word_tokenize(x)
    gender = [str(i) for i in x if i in headers]
    gender = set_list_convertor(gender)
    if len(gender) > 0:
        gender = ",".join(gender)
    else:
        gender = ""
    return gender