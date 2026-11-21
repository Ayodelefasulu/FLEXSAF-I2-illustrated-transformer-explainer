import tiktoken

# load two different tokenizers
tokenizers = {
	"GPT-2": tiktoken.get_encoding("gpt2"),
	"CL100K": tiktoken.get_encoding("cl100k_base"),
}


texts = [
    "The Lord is my shepherd.",
    "Artificial intelligence is transforming technology.",
    "Python is a popular programming language.",
    "Transformers use self-attention mechanisms.",
    "I am learning AI Engineering.",
]


# compare token counts
for text in texts:

    print("\nText:", text)

    for name, tokenizer in tokenizers.items():

        token_ids = tokenizer.encode(text)

        print(f"{name}: {len(token_ids)} tokens")

