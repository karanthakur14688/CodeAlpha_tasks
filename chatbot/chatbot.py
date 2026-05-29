def get_response(user_input):
    user_input = user_input.lower().strip()

    responses = {
        "hello": "Hi there! 😊 How can I help you?",
        "hi": "Hey! Good to see you! 👋",
        "how are you": "I'm doing great, thanks for asking! 😄 What about you?",
        "i am fine": "That's wonderful to hear! 😊",
        "what is your name": "I'm ChatBot 🤖 — your friendly Python chatbot!",
        "who made you": "I was built using Python with love 💻",
        "what can you do": "I can chat with you, answer basic questions, and keep you company! 😄",
        "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs! 🐛😂",
        "help": "You can say: hello, how are you, tell me a joke, what is your name, bye... and more!",
        "bye": "Goodbye! 👋 Have a great day!",
        "thanks": "You're welcome! 😊",
        "thank you": "Anytime! Happy to help 😄",
    }

    # Check for exact match
    if user_input in responses:
        return responses[user_input]

    # Check for partial/keyword match
    if "hello" in user_input or "hi" in user_input:
        return "Hey there! 👋"
    elif "your name" in user_input:
        return "I'm ChatBot 🤖!"
    elif "joke" in user_input:
        return "A programmer's wife says: 'Go to the market, get a litre of milk, and if they have eggs, get 12.' He came back with 12 litres of milk. 😂"
    elif "bye" in user_input or "exit" in user_input or "quit" in user_input:
        return "Goodbye! 👋 See you next time!"
    else:
        return "Hmm, I didn't get that 🤔 Type 'help' to see what I can do!"


def run_chatbot():
    print("=" * 40)
    print("       Welcome to ChatBot 🤖")
    print("  Your simple Python Chatbot!")
    print("  Type 'bye' or 'quit' to exit.")
    print("=" * 40)
    print()

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            print("Bot: Please type something! 😊\n")
            continue

        response = get_response(user_input)
        print(f"Bot: {response}\n")

        if user_input.lower() in ["bye", "exit", "quit"]:
            break


run_chatbot()