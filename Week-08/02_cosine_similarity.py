import math

word_vectors = {
    "cat": [1, 0],
    "kitten": [0.9, 0.1],
    "car": [0, 1],
}

def cosine_similarity(vector_a, vector_b):
    dot_product = 0
    squared_a = 0
    squared_b = 0

    for i in range(len(vector_a)):
        dot_product += vector_a[i] * vector_b[i]
        squared_a += vector_a[i] ** 2
        squared_b += vector_b[i] ** 2

    magnitude_a = math.sqrt(squared_a)
    magnitude_b = math.sqrt(squared_b)

    return dot_product / (magnitude_a * magnitude_b)


cat_kitten = cosine_similarity(
    word_vectors["cat"],
    word_vectors["kitten"]
)
cat_car = cosine_similarity(
    word_vectors["cat"],
    word_vectors["car"]
)
kitten_car = cosine_similarity(
    word_vectors["kitten"],
    word_vectors["car"]
)
print("Kitten vs car:", round(kitten_car, 4))
print("Cat vs kitten:", round(cat_kitten, 4))
print("Cat vs car:", round(cat_car, 4))