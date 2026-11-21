import tiktoken

#1. load the GPT-2 tokenizer
tokenizer = tiktoken.get_encoding("gpt2")

#2. define our sample sentences
texts = [
    "The Lord is my shepherd.",
    "Artificial intelligence is transforming technology.",
    "Python is a popular programming language.",
    "Transformers use self-attention mechanisms.",
    "I am learning AI Engineering.",
]

#3. process each sentence
for text in texts:

    # Convert text into token IDs
    token_ids = tokenizer.encode(text)

    # Convert token IDs into readable token pieces
    token_pieces = [
        tokenizer.decode_single_token_bytes(token_id).decode(
            "utf-8", errors="replace"
        )
        for token_id in token_ids
    ]

	# display the results
    print("=" * 70)
    print("Original text:", text)
    print("Token pieces:", token_pieces)
    print("Token IDs:", token_ids)
    print("Number of tokens:", len(token_ids))
