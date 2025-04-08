#====================================TASK-1====================================
# CHATBOT WITH RULE-BASED RESPONSES
def chatbot_response(user_input):
    # Convert input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Predefined rules
    if "hello" in user_input or "hi" in user_input:
        return "Hey there! I'm so glad to chat with you today. What's on your mind?"
    elif "how are you" in user_input:
        return "I'm doing great, thank you! As a bot, I stay positive. How are things with you?"
    elif "what is your name" in user_input or "your name" in user_input:
        return "My name is ChatBot 2.0, your friendly virtual assistant. What's yours?"
    elif "weather" in user_input:
        return "I don’t have live weather updates, but it’s a great idea to check a weather app!"
    elif "joke" in user_input:
        return "Sure! Why don’t scientists trust atoms? Because they make up everything!"
    elif "recommend a book" in user_input:
        return "I’d recommend 'Sapiens' by Yuval Noah Harari for a fascinating look at human history."
    elif "movie" in user_input or "recommend a movie" in user_input:
        return "If you're into adventure, go for 'Indiana Jones'! Or for something intense, try 'Inception'."
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Stay safe, take care, and come back whenever you'd like. 😊"
    elif "help" in user_input:
        return "Of course! I'm here to help. Let me know what's troubling you, and I'll do my best!"
    elif "programming" in user_input:
        return "Programming? Awesome! Are you working on Python, or exploring other languages?"
    else:
        return "I’m not sure I get that. Could you explain it differently? I’d love to help!"

def main():
    print("Chatbot: Hey there! I’m ChatBot AI, here to brighten your day. Type 'bye' to end our chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "goodbye"]:
            print("Chatbot: Goodbye! Stay safe, take care, and come back whenever you'd like. 😊")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()