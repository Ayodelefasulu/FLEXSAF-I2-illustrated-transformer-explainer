import tiktoken

def check_token_budget(
    text,
    context_limit,
    reserved_output,
    encoding_name="gpt2"
):
    tokenizer = tiktoken.get_encoding(encoding_name)

    token_ids = tokenizer.encode(text)

    input_tokens = len(token_ids)

    available_input = context_limit - reserved_output

    print("Token Budget Report")
    print("-" * 35)

    print("Input tokens:", input_tokens)
    print("Context limit:", context_limit)
    print("Reserved output tokens:", reserved_output)
    print("Available input tokens:", available_input)

    if input_tokens <= available_input:
        print("Status: Fits within the input budget")
    else:
        print("Status: Exceeds the input budget")



sample_text = """
    Large Language Models use neural networks,
    particularly Transformer architectures,
    to process and generate human language.
"""

check_token_budget(
    text=sample_text,
    context_limit=1024,
    reserved_output=200
)
