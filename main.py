from datetime import datetime


def get_response(message):
    message = message.strip().lower()

    if message in {"hello", "hi", "hey", "good morning", "good afternoon", "good evening"}:
        return "Hi! Welcome. How can I help you today?"
    if "how are you" in message:
        return "I'm fine, thanks for asking! How are you?"
    if "your name" in message or "who are you" in message:
        return "I'm PyBuddy, a simple rule-based Python chatbot."
    if "time" in message:
        return f"The current system time is {datetime.now().strftime('%I:%M %p')}."
    if "help" in message:
        return "You can say hello, ask how I am, ask my name, ask for the time, or type bye to exit."
    if message in {"bye", "goodbye", "exit", "quit"}:
        return "Goodbye! Have a great day."
    if "thank" in message:
        return "You're welcome!"
    return "I'm not sure how to respond to that yet. Try saying 'help' to see what I understand."


def main():
    print("=== PYBUDDY: BASIC CHATBOT ===")
    print("Chat with me! Type 'help' for examples or 'bye' to exit.")

    while True:
        user_message = input("\nYou: ").strip()
        if not user_message:
            print("PyBuddy: Please type a message.")
            continue

        response = get_response(user_message)
        print(f"PyBuddy: {response}")

        if user_message.lower().strip() in {"bye", "goodbye", "exit", "quit"}:
            break


if __name__ == "__main__":
    main()
