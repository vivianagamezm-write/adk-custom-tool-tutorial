"""Minimal Google ADK example for a custom function tool walkthrough."""

from google.adk.agents import Agent


def count_words(text: str) -> str:
    """Count the words in a piece of text.

    Args:
        text: The text whose words should be counted.

    Returns:
        A sentence containing the word count.
    """
    word_count = len(text.split())
    return f"The text contains {word_count} words."


root_agent = Agent(
    name="word_count_agent",
    model="gemini-2.5-flash",
    instruction=(
        "Help users with simple text questions. "
        "When asked to count words in text, use the count_words tool."
    ),
    tools=[count_words],
)
