import nltk
import urllib
import bs4 as bs
import re
import sys
import warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
import nltk

# Gettings the data source
my_url = input("Enter the URL you want to extract")
source = urllib.request.urlopen(my_url).read()

# Parsing the data/ creating BeautifulSoup object
soup = bs.BeautifulSoup(source,'lxml')

# Fetching the data
text = ""
for paragraph in soup.find_all('p'):
    text += paragraph.text

# Preprocessing the data
text = re.sub(r'\[[0-9]*\]',' ',text)
text = re.sub(r'\s+',' ',text)
text = text.lower()
text = re.sub(r'\d',' ',text)
text = re.sub(r'\s+',' ',text)

# Preparing the dataset
sentences = nltk.sent_tokenize(text)

sentences = [nltk.word_tokenize(sentence) for sentence in sentences]

with open("extract.txt", "w") as f:
    for sens in sentences:
        f.write(" ".join(sens))
with open("extract.txt", "r") as f:
    text_full = f.read()
