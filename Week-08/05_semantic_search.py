import torch
from sentence_transformers import SentenceTransformer, util

documents = [
    "The cat is sitting on the mat.",
    "A kitten is resting on a rug.",
    "A car is driving down the road.",
]

query = "A small kitten is taking a nap."

device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using device:", device)

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2",
    device=device
)

document_embeddings = model.encode(
    documents,
    convert_to_tensor=True
)
query_embedding = model.encode(
    query,
    convert_to_tensor=True
)

scores = util.cos_sim(query_embedding, document_embeddings)[0]

best_index = 0
best_score = scores[0].item()

for i in range(len(documents)):
    score = scores[i].item()
    print(round(score, 4), "-", documents[i])

    if score > best_score:
        best_score = score
        best_index = i

print("Best match:", documents[best_index])