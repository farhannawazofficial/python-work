import nltk
from nltk.chat.util import Chat, reflections

# Load the pre-trained chatbot pairs
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?"]
    ],
    [
        r"what is your name?",
        ["My name is chateBoat. I'm a chatbot here to assist you."]
    ],
    [
        r"(.*) your purpose",
        ["I'm designed to help you with various tasks and answer your questions."]
    ],
    [
        r"(.*) created you",
        ["I was created by a Farhan Nawaz."]
    ],
    # Add more pairs to expand the chatbot's capabilities
]

# Create a chat instance
chatbot = Chat(pairs, reflections)

# Start the conversation
chatbot.converse()
