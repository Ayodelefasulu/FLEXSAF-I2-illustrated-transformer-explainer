
# Prompting versus Fine-tuning

## Prompting

Prompting changes the instructions or context supplied to a pretrained
language model.

The model uses its existing learned parameters to generate a response.

No model weight updates occur during ordinary prompting.

Examples:
- Zero-shot prompting
- One-shot prompting
- Few-shot prompting
- Role-based instructions
- Structured output instructions

## Fine-tuning

Fine-tuning continues the training of a pretrained model using
additional task-specific or domain-specific data.

The training process updates selected model parameters.

Examples:
- Full fine-tuning
- Parameter-efficient fine-tuning (PEFT)
- LoRA

## Key Differences

| Prompting | Fine-tuning |
|---|---|
| Changes input instructions | Changes trainable parameters |
| No additional model training | Requires a training process |
| Usually quicker to experiment with | Requires training data and resources |
| Does not update model weights | Updates model weights or adapters |

## When to Use Each

Use prompting when instructions and examples are sufficient.

Consider fine-tuning when repeated task-specific behaviour or
specialised response patterns are difficult to achieve through
prompting alone.

Fine-tuning is not a substitute for RAG when the application needs
reliable access to changing external information.
