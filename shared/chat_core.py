from typing import Dict
from dotenv import load_dotenv

from shared.crews.crew_ai import CrewaiConversationalChatbotCrew

# Ensure environment variables are loaded for providers like OpenAI
load_dotenv()


def generate_chat_response(user_message: str) -> str:
    """Generate a chat response using the CrewAI crew.

    Args:
        user_message: The user's input message
    Returns:
        The AI assistant's response as a string
    """
    crew = CrewaiConversationalChatbotCrew()
    inputs: Dict[str, str] = {"user_message": user_message}
    result = crew.crew().kickoff(inputs=inputs)
    return str(result)