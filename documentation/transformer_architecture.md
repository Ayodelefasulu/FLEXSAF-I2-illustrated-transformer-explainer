
flowchart TD
    A["Raw Text"] --> B["Tokenizer"]
    B --> C["Token IDs"]
    C --> D["Token Embeddings"]
    D --> E["Add Positional Embeddings"]

    E --> F["Transformer Block 1"]

    F --> G["Transformer Block 2"]
    G --> H["..."]
    H --> I["Transformer Block N"]

    subgraph TB["Transformer Block"]
        J["Layer Normalization"]
        K["Masked Multi-Head Self-Attention"]
        L["Residual Connection"]
        M["Layer Normalization"]
        N["Feed-Forward Neural Network"]
        O["Residual Connection"]

        J --> K --> L --> M --> N --> O
    end

    I --> P["Final Layer Normalization"]
    P --> Q["Language Model Head"]
    Q --> R["Vocabulary Logits"]
    R --> S["Softmax / Decoding"]
    S --> U["Next Token"]
    U --> V["Append Token and Repeat"]
