
# LLM Limitations and Failure Modes

## 1. Hallucination

An LLM may generate plausible but false or unsupported information.

Mitigation:
- Retrieval-Augmented Generation
- Evidence verification
- Source citations
- Abstention when evidence is insufficient

## 2. Outdated Knowledge

A pretrained model may not know recent events or changes.

Mitigation:
- Web search
- External APIs
- Updated knowledge repositories

## 3. Bias

Models may reproduce biases present in training data.

Mitigation:
- Bias evaluation
- Diverse testing datasets
- Human oversight

## 4. Context Failure

A model may overlook important information even when it is
available within its context window.

Mitigation:
- Context management
- Document chunking
- Relevant retrieval
- Summarisation

## 5. Mathematical and Logical Errors

An LLM may produce incorrect calculations or reasoning.

Mitigation:
- Python execution
- Calculators
- Deterministic business logic
- Independent validation

## 6. Prompt Injection

Untrusted content may attempt to manipulate model behaviour.

Mitigation:
- Tool permission restrictions
- Input and output validation
- Separation of trusted instructions and untrusted data
- Backend authorisation checks

## Product Implications

LLM applications should not depend exclusively on model-generated
answers for critical operations.

Reliable applications combine language models with databases,
external APIs, retrieval systems, validation, monitoring and
appropriate human oversight.
