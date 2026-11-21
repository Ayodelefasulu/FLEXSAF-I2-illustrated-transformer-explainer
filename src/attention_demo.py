import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt
import seaborn as sns


#1. define five illustrative token representations
tokens = ["The", "animal", "crossed", "street", "it"]

torch.manual_seed(42)

# each token has a vector of 4 numerical values
X = torch.randn(5, 4)


#2. define trainable projection matrices
d_model = 4
d_k = 4

W_Q = torch.randn(d_model, d_k)
W_K = torch.randn(d_model, d_k)
W_V = torch.randn(d_model, d_k)



#3. calculate Query, Key and Value
Q = X @ W_Q
K = X @ W_K
V = X @ W_V


#4. calculate attention scores
scores = Q @ K.T / (d_k ** 0.5)


#5. apply causal mask
mask = torch.triu(
	torch.ones(5, 5),
	diagonal=1
).bool()

scores = scores.masked_fill(mask, float("-inf"))


#6. calculate attention weights
attention_weights = F.softmax(scores, dim=-1)


#7. calculate attention output
attention_output = attention_weights @ V


#8. display results
print("input shape:", X.shape)
print("query shape:", Q.shape)
print("key shape:", K.shape)
print("value shape:", V.shape)
print("attention weights shape:", attention_weights.shape)
print("attention output shape:", attention_output.shape)

