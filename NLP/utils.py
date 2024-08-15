import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def clean_html(text):
   clean = re.compile('<.*?>')
   return re.sub(clean,'',text)

def convert_lower(text):
   return text.lower()

def remove_special(text):
   x = ''
   for i in text:
      if i.isalnum():
         x = x + i
      else:
         x = x + ' '
   return x

def remove_stopwords(text):
   x = []
   for i in text.split():
      if i not in stopwords.words('english'):
         x.append(i)
   y = x[:]
   x.clear()
   return y

ps = PorterStemmer()
y = []
def stem_words(text):
   for i in text:
      y.append(ps.stem(i))
   z = y[:]
   y.clear()
   return z

def join_back(list_input):
   return " ".join(list_input)