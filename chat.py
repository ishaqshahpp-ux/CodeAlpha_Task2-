# Simple Rule-Based Chatbot

def chatbot():
    print("Chatbot: Hello! Type 'bye' to end the chat.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Chatbot: Hi!")

        elif user_input == "how are you":
            print("Chatbot: I am fine, thank you!")

        elif user_input == "what is your name":
            print("Chatbot: I am a simple chatbot.")

        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break

        else:
            print("Chatbot: Sorry, I don't understand.")

# Run the chatbot
chatbot()