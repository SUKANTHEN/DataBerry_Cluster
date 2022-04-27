import re

#mastercard_regex = 

keys_for_validation = {"aadhaar_card":"^[2-9]{1}[0-9]{3}\\s[0-9]{4}\\s[0-9]{4}$",
                       "pancard":"[A-Z]{5}[0-9]{4}[A-Z]{1}",
                       "ind_drivinglicense":"^(([A-Z]{2}[0-9]{2})( )|([A-Z]{2}-[0-9]{2}))((19|20)[0-9][0-9])[0-9]{7}$",
                       "social_security_number": "^(?!666|000|9\\d{2})\\d{3}-(?!00)\\d{2}-(?!0{4})\\d{4}$",
                       "visacard":"^4[0-9]{12}(?:[0-9]{3})?$"}

def Document_Number_validator(regex_str,string):
    op = re.compile(regex_str)
    if (str == None):
        return 0
    if(re.search(op, string)):
        return 1
    else:
        return 0