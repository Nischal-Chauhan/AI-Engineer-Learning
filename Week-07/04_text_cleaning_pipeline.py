import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

text = "The students are learning from books, and books are useful."

# Lowercase aur punctuation removal
clean_text = text.lower()
clean_text = clean_text.translate(
    str.maketrans("", "", string.punctuation)
)

# Tokenization: text ko words ki list mein todna
tokens = clean_text.split()

# Common stopwords hatana
stop_words = set(stopwords.words("english"))
filtered_tokens = [
    word for word in tokens if word not in stop_words
]

# Stemming aur lemmatization ke results alag-alag dekhna
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_tokens]

lemmatizer = WordNetLemmatizer()
lemmatized_words = [
    lemmatizer.lemmatize(word) for word in filtered_tokens
]

print("Original text:", text)
print("Tokens:", tokens)
print("After removing stopwords:", filtered_tokens)
print("Stemmed words:", stemmed_words)
print("Lemmatized words:", lemmatized_words)