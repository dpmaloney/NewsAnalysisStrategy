from textblob import TextBlob
from bs4 import BeautifulSoup
import requests

class Analysis:
	def __init__(self, term, day, month, year):
		self.term = term
		self.sentiment = 0
		self.subjectivity = 0
		startday = day-2
		endday = day-1
		self.url = 'https://www.google.com/search?q={0}&source=lws&tbs=cdr%3A1%2Ccd_min%3A{3}%2F{1}%2F{5}%2Ccd_max%3A{4}%2F{2}%2F{6}&tbm=nws'.format(self.term, startday, endday, month, month, year, year)

	def run(self):
		response = requests.get(self.url)
		soup = BeautifulSoup(response.text, 'html.parser')
		headline_results = soup.find_all('div', class_='st')
		for text in headline_results:
			blob = TextBlob(text.get_text())	
			self.sentiment += blob.sentiment.polarity / len(headline_results)
			self.subjectivity += blob.sentiment.subjectivity / len(headline_results)

a = Analysis('bitcoin', 29, 6, 2019)
a.run()

print(a.sentiment)