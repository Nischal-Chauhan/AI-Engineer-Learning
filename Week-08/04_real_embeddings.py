import torch
from sentence_transformers import SentenceTransformer, util

sentences = [
    "The cat is sitting on the mat.",
    "A kitten is resting on a rug.",
    "A car is driving down the road.",
]

device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using device:", device)

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2",
    device=device
)

embeddings = model.encode(
    sentences,
    convert_to_tensor=True
)

print("Embedding shape:", embeddings.shape)
print(
    "Cat vs kitten:",
    round(util.cos_sim(embeddings[0], embeddings[1]).item(), 4)
)
print(
    "Cat vs car:",
    round(util.cos_sim(embeddings[0], embeddings[2]).item(), 4)
)