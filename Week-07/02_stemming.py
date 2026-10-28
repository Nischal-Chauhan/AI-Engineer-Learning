from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
words = ["running", "plays", "happily", "studies"]

for word in words:
    stemmed_word = stemmer.stem(word)
    print(word, "->", stemmed_word)