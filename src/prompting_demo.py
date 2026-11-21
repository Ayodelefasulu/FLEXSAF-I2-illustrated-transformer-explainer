
# Simulated customer complaint
complaint = """
I paid for my subscription, but my account still says unpaid.
"""


# Prompting approach
prompt = f"""
You are a customer support assistant.

Classify the complaint into:
- Billing
- Technical
- Account Access

Recommend an appropriate action.

Complaint:
{complaint}
"""


print("PROMPTING DEMONSTRATION")
print("-" * 40)
print(prompt)


# Simulated model configuration
model_parameters = {
    "temperature": 0.2,
    "model_weights_updated": False
}


print("\nModel configuration:")
print(model_parameters)


# Demonstrate a change in instructions
improved_prompt = f"""
You are a customer support assistant.

Return your answer in this format:
Category: <category>
Priority: <priority>
Suggested action: <action>

Complaint:
{complaint}
"""


print("\nIMPROVED PROMPT")
print("-" * 40)
print(improved_prompt)

print("\nWere model weights updated?")
print(model_parameters["model_weights_updated"])

