import json
from datetime import datetime

# Initialize an empty list to store conversation messages
conversation = []

def add_message(sender, message):
   
    conversation.append({
        "User": sender,
        "Bot": message
    })

def save_conversation_to_json(filename="conversation.json"):
   
    with open(filename, 'a') as file:
        json.dump(conversation, file, indent=4)
    print(f"Conversation saved to {filename}")

# Example usage:
while True :
    
    user_input = input("User : ")
    if user_input == "q" :
        save_conversation_to_json()
        break
    add_message("User1", user_input)
    bot =  input("Bot messsage : ")
    add_message("User2", bot)
    


# Save the conversation to a JSON file

