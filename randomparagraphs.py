file_path = "C:/Users/DELL/Desktop/cloud/random_paragraphs.txt.txt"  
with open(file_path, 'r') as file:
    random_paragraphs = file.readlines()   
for line in random_paragraphs[:5]:  
    print(line)
print(type(random_paragraphs))

import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
",".join(stopwords.words('english'))

stop_words=set(stopwords.words('english'))

filtered_sentences = []
for sentence in random_paragraphs:
    words = sentence.lower().split()
    filtered_words = [word for word in words if word not in stop_words]
    filtered_sentence = " ".join(filtered_words)
    filtered_sentences.append(filtered_sentence)

for line in filtered_sentences[:15]: 
    print(line)
from collections import Counter


text = ' '.join(filtered_sentences)
words = text.split()

word_frequency = Counter(words)

for word, frequency in word_frequency.items():
    print(f"Word: {word}, Frequency: {frequency}")