from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

words_and_types = [
    ("cars", "n"),
    ("children", "n"),
    ("running", "v"),
    ("studies", "v"),
]

for word, word_type in words_and_types:
    base_word = lemmatizer.lemmatize(word, pos=word_type)
    print(word, "->", base_word)