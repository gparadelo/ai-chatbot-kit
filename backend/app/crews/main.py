from crew_ai import CrewaiConversationalChatbotCrew
from dotenv import load_dotenv

load_dotenv()

def run():
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye! It was nice talking to you.")
            break

        inputs = {
            "user_message": f"{user_input}",
        }

        response = CrewaiConversationalChatbotCrew().crew().kickoff(inputs=inputs)
        print(f"Assistant: {response}")

# Add this block to actually run the function
if __name__ == "__main__":
    run()