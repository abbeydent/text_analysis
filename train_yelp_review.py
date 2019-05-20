import json
import pandas as pd 
import string

import nltk

from nltk.corpus import stopwords
nltk.download('stopwords')

from nltk.stem import WordNetLemmatizer

review_text = []
review_stars = []
with open('yelp_review_part1.json') as f:
	for line in f:
		json_line = json.loads(line)
		review_text.append(json_line["text"])
		review_stars.append(json_line["stars"])

dataset = pd.DataFrame(data = {'text': review_text, 'stars': review_stars})#, columns=['text', 'stars'])

print(dataset.shape)

dataset = dataset[0:3000]

print(dataset.shape)

dataset = dataset[(dataset['stars']==1)|(dataset['stars']==5)]

print(dataset.shape)

data = dataset['text']
target = dataset['stars']

lemmatizer = WordNetLemmatizer()

def pre_processing(text):
	text_processed = [char for char in text if char not in string.punctuation]
	text_processed = ''.join(text_processed)
	return [lemmatizer.lemmatize(word.lower()) for word in text_processed.split() if word.lower() not in stopwords.words('english')]

print(pre_processing("This is some text. Hello!!! This is pretending to be a review. Reviews are funny."))

