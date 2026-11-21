
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt


# 1. Define our sentences
sentences = [
    "A dog is playing in the garden.",
    "A puppy is running outside.",
    "A cat is sleeping on the sofa.",
    "The government announced a new policy.",
    "A car is driving along the highway."
]


# 2. Load a pretrained sentence embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# 3. Convert sentences into numerical vectors
embeddings = model.encode(sentences)


# 4. Inspect the embedding dimensions
print("Embedding shape:", embeddings.shape)


# 5. Calculate cosine similarity
similarity_matrix = cosine_similarity(embeddings)


# 6. Display similarity results
df = pd.DataFrame(
    similarity_matrix,
    index=["Sentence 1", "Sentence 2", "Sentence 3",
           "Sentence 4", "Sentence 5"],
    columns=["Sentence 1", "Sentence 2", "Sentence 3",
             "Sentence 4", "Sentence 5"]
)

print("\nCosine Similarity Matrix:")
print(df.round(3))


# 7. Reduce embeddings from 384 dimensions to 2 dimensions
pca = PCA(n_components=2)

reduced_embeddings = pca.fit_transform(embeddings)


# 8. Visualise the embeddings
plt.figure(figsize=(10, 7))

for i, sentence in enumerate(sentences):

    x = reduced_embeddings[i, 0]
    y = reduced_embeddings[i, 1]

    plt.scatter(x, y)

    plt.annotate(
        f"Sentence {i + 1}",
        (x, y),
        xytext=(5, 5),
        textcoords="offset points"
    )

plt.title("Sentence Embeddings Visualisation using PCA")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.grid(True)
plt.tight_layout()

plt.savefig("diagrams/embedding_visualisation.png")
plt.show()
