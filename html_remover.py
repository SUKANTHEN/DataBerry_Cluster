import re
###############################################
# Function to remove html tags from text input#
def cleanhtml(raw_data):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_data)
    return cleantext
###############################################