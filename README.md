# Illustrated Transformer Explainer

An educational Python project that demonstrates the core concepts behind Large Language Models (LLMs), with a focus on tokenisation, embeddings, attention, Transformer architecture, context windows, prompting, and output validation.

The project combines executable Python demonstrations with conceptual documentation to explain how Transformer-based language models process and generate text.

## Project Objectives

This project was developed to build practical understanding of:

- How text is converted into tokens and token IDs.
- How tokens are represented as numerical embeddings.
- How semantic similarity can be explored using sentence embeddings.
- How Query, Key, and Value vectors contribute to self-attention.
- How causal masking prevents a decoder from attending to future tokens.
- How a Transformer processes token representations.
- How context-window limits affect LLM applications.
- The difference between prompting and fine-tuning.
- Common LLM failure modes and ways to validate model outputs.

## Project Structure

```text
i2-illustrated-transformer-explainer/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── diagrams/
├── notebooks/
│
├── src/
│   ├── tokenizer_demo.py
│   ├── tokenizer_comparison.py
│   ├── token_budget.py
│   ├── embedding_similarity.py
│   ├── attention_demo.py
│   ├── context_window_demo.py
│   ├── prompting_demo.py
│   └── output_validation_demo.py
│
└── documentation/
    ├── transformer_explanation.md
    ├── transformer_architecture.md
    ├── context_window_explanation.md
    ├── prompting_vs_finetuning.md
    └── limitations_and_failure_modes.md
```

## Technologies

- Python
- PyTorch
- tiktoken
- Sentence Transformers
- scikit-learn
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Pydantic
- Jupyter Notebook

## Getting Started

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd i2-illustrated-transformer-explainer
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Linux or macOS:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the demonstrations

For example:

```bash
python src/tokenizer_demo.py
```

Other demonstrations can be executed individually:

```bash
python src/tokenizer_comparison.py
python src/token_budget.py
python src/embedding_similarity.py
python src/attention_demo.py
python src/context_window_demo.py
python src/prompting_demo.py
python src/output_validation_demo.py
```

Some demonstrations, particularly the sentence-embedding example, may download a pretrained model the first time they run. An internet connection may be required for that initial download.

## Demonstrations

| Demonstration | What it explores |
|---|---|
| Tokenisation | Text, token pieces, and token IDs |
| Tokenizer comparison | Differences in token counts |
| Token budget | Estimating input capacity |
| Embedding similarity | Sentence vectors and cosine similarity |
| Attention | Q, K, V, causal masking, and attention weights |
| Context window | Token limits and chunking |
| Prompting | How instructions influence model behaviour |
| Output validation | Using Pydantic to validate structured outputs |

## Transformer Architecture

The project documentation explains a simplified GPT-style decoder-only Transformer:

1. Input text is tokenised.
2. Token IDs are mapped to token embeddings.
3. Positional information is added.
4. Transformer blocks process the representations.
5. Each block applies masked multi-head self-attention and a feed-forward network, with residual connections and normalisation.
6. The language-model head produces vocabulary logits.
7. A decoding strategy selects the next token.

See [Transformer Architecture](documentation/transformer_architecture.md) for the architecture diagram and [Transformer Explanation](documentation/transformer_explanation.md) for the detailed explanation.

## Important Educational Limitations

This project is an educational collection of demonstrations, not a complete production LLM.

- The attention demonstration uses randomly generated tensors and randomly initialised projection matrices. It illustrates the attention calculation; it does not demonstrate learned language understanding.
- The prompting demonstration is a conceptual simulation, not a live interaction with an LLM.
- The embedding demonstration uses a pretrained sentence-embedding model. Its vectors are not the same as the internal token embeddings of GPT-2.
- The context-window demonstration uses a simplified token limit to illustrate token budgeting.
- Output validation checks whether structured data conforms to a defined schema. It does not establish whether the content is factually correct.

These distinctions are important when interpreting the results.

## Learning Outcomes

Through this project, I explored the relationship between tokenisation, numerical representations, attention mechanisms, Transformer blocks, and the behaviour of modern LLM applications.

I also examined practical engineering concerns such as token budgeting, structured output validation, model limitations, and the role of external tools and retrieval systems in building more reliable AI applications.

## Future Improvements

Potential extensions include:

- Implementing a small Transformer model using PyTorch.
- Comparing attention weights from a pretrained Transformer.
- Building a small next-token prediction demonstration.
- Connecting a language model through an inference API.
- Implementing a simple Retrieval-Augmented Generation (RAG) workflow.
- Adding automated tests for the demonstration scripts.

## Project Status

Educational project — I2: Deep Learning and Transformer Foundations.

The demonstrations are intended to make important Transformer and LLM concepts easier to understand through code, diagrams, and explanations.
