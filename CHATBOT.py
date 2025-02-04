import spacy
import random
import re

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

responses = {
    r"\bhi\b": ["Hello!", "Hi there! How's it going?", "Hey! How can I help you?"],
    r"\bhow are you\b": ["I'm doing well, thank you! How about you?", "I'm great, thanks for asking! What's up with you?"],
    r"\bbye\b": ["Goodbye! See you later!", "Bye! Take care!", "Talk to you soon!"],
    r"\bhelp\b": ["What do you need help with?", "I'm here to assist you. How can I help?"],
    r"\btime\b": ["Sorry, I can't check the time. Please check your device."],
    r"\bwhat is your name\b": ["I’m Chatbot! Your friendly virtual assistant.", "You can call me Chatbot!"],
    r"\bthank you\b": ["You're welcome!", "Happy to help!", "No problem!"],
    r"\bwhat do you do\b": ["I help you with anything you need, from chatting to answering questions.", "I'm here to assist you however I can!"],
    r"\bwhere are you from\b": ["I’m a virtual assistant, so I don’t have a physical location, but I’m always here to chat!"],
    r"\bhow old are you\b": ["I don’t have a specific age, but I was created recently to help you."],
    r"\bweather\b": ["I can't check the weather, but you can check your device or website for the most up-to-date info."],
    r"\bcool\b": ["Glad you think so!", "Thanks, I try my best!"],
    r"\bwhat can you do\b": ["I can chat, answer questions, and help with various tasks. Ask me anything!", "I'm here to assist with any queries you have."],
    r"\bhello\b": ["Hi there! How's everything?", "Hello! How can I assist you today?"],
    r"\bhow's it going\b": ["It’s going great, thanks for asking! How about you?", "Everything's going well, thanks! What's new with you?"],
    r"\bthank you for helping\b": ["You're welcome! Let me know if you need anything else.", "Happy to help! Feel free to ask anything."]
}

user_data = {}  # To store information about the user (e.g., name, mood)

def chatbot():
    print("Chatbot: Hi! How can I assist you today?")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye! Talk to you soon!")
            break
        
        # Process user input with spaCy for better understanding
        doc = nlp(user_input)
        
        # Identify named entities or parts of speech (e.g., people's names, places, etc.)
        named_entities = [ent.text for ent in doc.ents]
        if named_entities:
            print(f"Chatbot: I see you're talking about {', '.join(named_entities)}.")
        
        response_found = False
        
        # Check for a known pattern in user input
        for pattern, replies in responses.items():
            if re.search(pattern, user_input):  # Check if any pattern matches the input
                print(f"Chatbot: {random.choice(replies)}")
                response_found = True
                break
        
        # Personalization: Respond based on previously gathered information
        if 'name' in user_data:
            print(f"Chatbot: It's nice to talk to you again, {user_data['name']}!")
        
        # Ask follow-up questions based on user mood or input
        if 'mood' in user_data:
            print(f"Chatbot: You seem {user_data['mood']} today! Anything I can do to brighten your day?")

        if not response_found:
            print("Chatbot: I'm sorry, I didn't understand that. Could you clarify or ask something else?")
        
        # Context tracking: Ask for the user's name and mood
        if 'name' not in user_data:
            if re.search(r'\bwhat is your name\b', user_input):
                user_name = input("Chatbot: What's your name? ")
                user_data['name'] = user_name
                print(f"Chatbot: Nice to meet you, {user_name}!")
        
        if 'mood' not in user_data:
            if re.search(r'\bhow are you\b', user_input):
                mood = input("Chatbot: How are you feeling today? ")
                user_data['mood'] = mood
                print(f"Chatbot: Got it, you're feeling {mood}. Thanks for sharing!")
        
if __name__ == "__main__":
    chatbot()
