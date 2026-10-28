import string

text = "  Python is GREAT for Text Processing! Let's learn NLP.  "

clean_text = text.strip().lower()

punctuation_table = str.maketrans("", "", string.punctuation)
clean_text = clean_text.translate(punctuation_table)

words = clean_text.split()
stop_words = {"is", "for"}
filtered_words = [word for word in words if word not in stop_words]

print("Words after removing stopwords:", filtered_words)

print("Clean text:", clean_text)
print("Words:", words)