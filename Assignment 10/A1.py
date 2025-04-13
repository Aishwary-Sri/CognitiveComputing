import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter

text = "Books open up new worlds. Reading improves vocabulary and knowledge. Many people enjoy fiction. Non-fiction is also popular. Libraries offer free access to books."

t1 = re.sub(r'[^a-zA-Z\s]', '', text.lower())
words1 = t1.split()
words2 = word_tokenize(t1)
sents = sent_tokenize(text)
stop_words = set(stopwords.words('english'))
filtered = [w for w in words2 if w not in stop_words]
freq = Counter(filtered)
print(freq)
