
import tiktoken


# 1. Load tokenizer
tokenizer = tiktoken.get_encoding("gpt2")


# 2. Define a hypothetical context limit
context_limit = 128


# 3. Create sample text
sample_text = """
Large Language Models are neural networks trained to process
and generate human language.

Transformer architectures use self-attention mechanisms to
learn relationships between tokens.

The attention mechanism calculates Query, Key and Value
representations and combines information across token positions.

Feed-forward networks further transform the representations
produced by attention.

During training, the model learns its parameters through
forward propagation, loss calculation, backpropagation,
and optimisation.

During inference, the trained model generates text
autoregressively by predicting one token at a time.
"""


# 4. Tokenise the text
token_ids = tokenizer.encode(sample_text)


# 5. Calculate token count
total_tokens = len(token_ids)


print("Context Window Demonstration")
print("-" * 40)

print("Total tokens:", total_tokens)
print("Context limit:", context_limit)


# 6. Check whether the text fits
if total_tokens <= context_limit:

    print("Status: Text fits within the context window")

else:

    print("Status: Text exceeds the context window")


# 7. Demonstrate truncation
truncated_tokens = token_ids[:context_limit]

truncated_text = tokenizer.decode(truncated_tokens)

print("\nTruncated token count:", len(truncated_tokens))
print("Truncated text:")
print(truncated_text)


# 8. Demonstrate chunking
chunk_size = 50
overlap = 10

step = chunk_size - overlap

chunks = []

for start in range(0, len(token_ids), step):

    chunk = token_ids[start:start + chunk_size]

    if not chunk:
        break

    chunks.append(chunk)


print("\nChunking Results")
print("-" * 40)

print("Number of chunks:", len(chunks))

for i, chunk in enumerate(chunks):

    print(f"\nChunk {i + 1}")
    print("Token count:", len(chunk))
    print("Text:", tokenizer.decode(chunk))
