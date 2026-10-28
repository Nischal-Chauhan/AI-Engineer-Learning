import math

sentences = [
    "car",
    "automobile",
    "car",
]

vocabulary = []

for sentence in sentences:
    for word in sentence.split():
        if word not in vocabulary:
            vocabulary.append(word)

sentence_vectors = []

for sentence in sentences:
    words = sentence.split()
    vector = []

    for word in vocabulary:
        vector.append(words.count(word))

    sentence_vectors.append(vector)

print("Vocabulary:", vocabulary)

for i in range(len(sentences)):
    print(sentences[i], "->", sentence_vectors[i])


def cosine_similarity(vector_a, vector_b):
    dot_product = 0
    squared_a = 0
    squared_b = 0

    for i in range(len(vector_a)):
        dot_product += vector_a[i] * vector_b[i]
        squared_a += vector_a[i] ** 2
        squared_b += vector_b[i] ** 2

    return dot_product / (
        math.sqrt(squared_a) * math.sqrt(squared_b)
    )


similarity = cosine_similarity(sentence_vectors[0], sentence_vectors[1])
print("Similarity of the first two sentences:", round(similarity, 4))

similarity = cosine_similarity(sentence_vectors[0], sentence_vectors[2])
print("Similarity of the first and third sentences:", round(similarity, 4))