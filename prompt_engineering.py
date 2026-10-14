
# Day 2 - Dynamic Prompt Engineering

MASTER_PROMPT = """
You are a professional enterprise customer service assistant.
Only answer using the context provided.
If the answer is not available in the context, clearly say
that the provided context does not contain the answer.

Context:
{context}

User Question:
{user_query}

Answer:
"""


def compile_prompt(context, query):
    prompt = MASTER_PROMPT.format(
        context=context,
        user_query=query
    )
    return prompt


if __name__ == "__main__":
    sample_context = "Our customer support team is available from 9 AM to 5 PM."
    sample_query = "What are the customer support hours?"

    final_prompt = compile_prompt(sample_context, sample_query)

    print("=== Generated Prompt ===")
    print(final_prompt)

# Task 3 - Mock Claude API Response Parsing

def mock_claude_response():
    """Simulate a response from the Claude API."""
    return {
        "content": [
            {
                "text": "Our customer support team is available from 9 AM to 5 PM."
            }
        ],
        "usage": {
            "input_tokens": 45,
            "output_tokens": 120
        }
    }


def extract_response(response):
    """Safely extract response text and token usage."""

    # Safely get the content list
    content = response.get("content", [])

    # Safely get text from the first content block
    first_block = content[0] if content else {}
    response_text = first_block.get("text", "No response text available.")

    # Safely get token usage
    usage = response.get("usage", {})
    input_tokens = usage.get("input_tokens", 0)
    output_tokens = usage.get("output_tokens", 0)

    # Calculate total tokens
    total_tokens = input_tokens + output_tokens

    # Return extracted information
    return {
        "response_text": response_text,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": total_tokens
    }


# Run Task 3
if __name__ == "__main__":
    mock_response = mock_claude_response()
    metadata = extract_response(mock_response)

    print("\n=== Mock Claude API Response ===")
    print("Response:", metadata.get("response_text"))

    print("\n=== Token Usage Metadata ===")
    print("Input tokens:", metadata.get("input_tokens"))
    print("Output tokens:", metadata.get("output_tokens"))
    print("Total tokens:", metadata.get("total_tokens"))
