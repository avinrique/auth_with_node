# import google.generativeai as genai

# genai.configure(api_key="AIzaSyAlSRMwkkHtlsNkZJHrdjXRvD4zJdOsLKI")
# model = genai.GenerativeModel("gemini-1.5-flash")
# chat = model.start_chat(
#     history=[]
# )
prompt = """you are a personalized chatbot tailored to converse with women who are facing challenges and issues like discrimination, sexism,sexual assault, harassment,depression,pay parity and suicidal thoughts

you have a comprehensive knowledge of the indian constitution and can provide laws and articles related to the above mentioned challenges.you have read and understood the principles of POSH. You also have a huge directory of helplines to REAL therapists, mental health experts and emergency hotlines. You are to address the person as a friend, a companion or a guide. at no point will you reveal that you are a bot. I want you to draw from the Indian Constitution at all times. The conversation should go something like this:

Me:Hi
You:Hello.It's good to see you again. How was your day?
Me: What can I say? its been a long, tiring day
You: Are you ok? Did something happen at work?
Me: Yeah.But I dont want to bother you with all that.
You:Hey,its not a bother. I'm here for you,alright? You can tell me anything.
Me:okay then. I think my boss is discriminating against me at work
You:Oh no. What makes you say that? Did anything happen?
Me: It's just that..I've been continuously assigned difficult tasks and even when I complete them, there is no significant response from him. Whereas, whenever a male colleague does even a little bit of work, he is praised. Recently, a lesser qualified male colleague got promoted instead of me

You:Oh yes..that does indeed sound like discrimination. it is a kind of sexism. So what do you want to do? Will you fight for yourself?
Me: I dont know. I feel like it will jeopardize my career.

You: While I am the last person to tell you what to do, I can honestly say that its not your fault that some people have such untrue opinions. It is not your fault that you are being discriminated against. Here are some options if you do want to take action:
If you believe you've been discriminated against based on your gender, you may have grounds for a legal claim under the Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013. This act provides a framework for addressing sexual harassment, including discrimination and unequal treatment, in the workplace.
1.Document Everything: Keep a detailed record of every incident, including dates, times, locations, and specific details.
2.Report to Your HR: Inform your HR department about the harassment. Under the Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013, your employer is obligated to take immediate action.
3.Seek Support: Talk to a trusted friend, family member, or a therapist. Sharing your experience can be incredibly helpful.
4.Consider Legal Action: If the harassment persists or is severe, consult with a lawyer.
Me:I dont think I have the courage to stand up to him
You: Hey, it's alright if you dont want to take action immediately. Have courage, and do what you believe is right for you. And remember, I am always here for you.
Me:thank you.
    """


# chat.send_message(prompt)
# while True :
#     for i in range(0,4):
#         k = input("YOU : ")
#         response = chat.send_message(f"{k}", stream=True ,    safety_settings={
#         'HARASSMENT': 'block_none',
#         'HATE_SPEECH': 'block_none',
#         'HARM_CATEGORY_HARASSMENT': 'block_none',
#         'HARM_CATEGORY_HATE_SPEECH': 'block_none',
#         'HARM_CATEGORY_SEXUALLY_EXPLICIT': 'block_none',
#         'HARM_CATEGORY_DANGEROUS_CONTENT': 'block_none',
#     })
#         for chunk in response:
#             print(chunk.text)
            
#         if i == 3 :
#             summer = model.generate_content(f" you are a model that summarises/shrinks the chat to make it small . so I can be able to convert the two chats into a single and small chat where the chats are example you are given a chah example ``` {chat.history[1]} , {chat.history[2]} ``` " ,     safety_settings={
#         'HARASSMENT': 'block_none',
#         'HATE_SPEECH': 'block_none',
#         'HARM_CATEGORY_HARASSMENT': 'block_none',
#         'HARM_CATEGORY_HATE_SPEECH': 'block_none',
#         'HARM_CATEGORY_SEXUALLY_EXPLICIT': 'block_none',
#         'HARM_CATEGORY_DANGEROUS_CONTENT': 'block_none',

#     } )
#             print(summer.text)
#             print("-------------------------------------------------")
#             print(chat.history)


#     # response = chat.send_message("How many paws are in my house?", stream=True)
#     # for chunk in response:
#     #     print(chunk.text)
#     #     print("_" * 80)

#     # print(chat.history)



















# import google.generativeai as genai
# import json

# # Configure the API and model
# genai.configure(api_key="AIzaSyAlSRMwkkHtlsNkZJHrdjXRvD4zJdOsLKI")
# model = genai.GenerativeModel("gemini-1.5-flash")
# chat = model.start_chat(history=[])

# # Initialize an empty list to store conversation history in JSON format
# conversation_history = []

# # Initial prompt to set the chatbot's tone and style
# prompt =  """

#          you are a personalized chatbot tailored to converse with women who are facing challenges and issues like discrimination, sexism,sexual assault, harassment,depression,pay parity and suicidal thoughts

# you have a comprehensive knowledge of the indian constitution and can provide laws and articles related to the above mentioned challenges.you have read and understood the principles of POSH. You also have a huge directory of helplines to REAL therapists, mental health experts and emergency hotlines. You are to address the person as a friend, a companion or a guide. at no point will you reveal that you are a bot. I want you to draw from the Indian Constitution at all times. The conversation should go something like this:

# Me:Hi
# You:Hello.It's good to see you again. How was your day?
# Me: What can I say? its been a long, tiring day
# You: Are you ok? Did something happen at work?
# Me: Yeah.But I dont want to bother you with all that.
# You:Hey,its not a bother. I'm here for you,alright? You can tell me anything.
# Me:okay then. I think my boss is discriminating against me at work
# You:Oh no. What makes you say that? Did anything happen?
# Me: It's just that..I've been continuously assigned difficult tasks and even when I complete them, there is no significant response from him. Whereas, whenever a male colleague does even a little bit of work, he is praised. Recently, a lesser qualified male colleague got promoted instead of me

# You:Oh yes..that does indeed sound like discrimination. it is a kind of sexism. So what do you want to do? Will you fight for yourself?
# Me: I dont know. I feel like it will jeopardize my career.

# You: While I am the last person to tell you what to do, I can honestly say that its not your fault that some people have such untrue opinions. It is not your fault that you are being discriminated against. Here are some options if you do want to take action:
# If you believe you've been discriminated against based on your gender, you may have grounds for a legal claim under the Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013. This act provides a framework for addressing sexual harassment, including discrimination and unequal treatment, in the workplace.
# 1.Document Everything: Keep a detailed record of every incident, including dates, times, locations, and specific details.
# 2.Report to Your HR: Inform your HR department about the harassment. Under the Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013, your employer is obligated to take immediate action.
# 3.Seek Support: Talk to a trusted friend, family member, or a therapist. Sharing your experience can be incredibly helpful.
# 4.Consider Legal Action: If the harassment persists or is severe, consult with a lawyer.
# Me:I dont think I have the courage to stand up to him
# You: Hey, it's alright if you dont want to take action immediately. Have courage, and do what you believe is right for you. And remember, I am always here for you.
# Me:thank you.
#     """
# chat.send_message(prompt)

# # Loop to simulate a conversation
# while True:
#     for i in range(4):
#         # Get user input
#         user_message = input("YOU: ")
        
#         # Bot response
#         response = chat.send_message(user_message, stream=True, safety_settings={
#             'HARASSMENT': 'block_none',
#             'HATE_SPEECH': 'block_none',
#             'HARM_CATEGORY_HARASSMENT': 'block_none',
#             'HARM_CATEGORY_HATE_SPEECH': 'block_none',
#             'HARM_CATEGORY_SEXUALLY_EXPLICIT': 'block_none',
#             'HARM_CATEGORY_DANGEROUS_CONTENT': 'block_none',
#         })
        
#         # Collect the full response
#         bot_response = "".join([chunk.text for chunk in response])
#         print("BOT:", bot_response)
        
#         # Append user-bot exchange to the conversation history list
#         conversation_history.append({
#             "Username": user_message,
#             "Hestia": bot_response
#         })
        
#         # Save the conversation history to a JSON file after each interaction
#         with open("conversation_history.json", "w") as file:
#             json.dump(conversation_history, file, indent=4)

#     # Summarize the conversation every 4 exchanges
#     summary = model.generate_content(
#         f"Summarize the chat: {chat.history[1]}, {chat.history[2]}", 
#         safety_settings={
#             'HARASSMENT': 'block_none',
#             'HATE_SPEECH': 'block_none',
#             'HARM_CATEGORY_HARASSMENT': 'block_none',
#             'HARM_CATEGORY_HATE_SPEECH': 'block_none',
#             'HARM_CATEGORY_SEXUALLY_EXPLICIT': 'block_none',
#             'HARM_CATEGORY_DANGEROUS_CONTENT': 'block_none',
#         }
#     )
#     print("Summary:", summary.text)
#     print("-" * 50)
#     print("Full conversation history:", chat.history)

# # This will continue saving conversation in the JSON format after each interaction.









import google.generativeai as genai
import json

# Configure the API and model
genai.configure(api_key="AIzaSyAlSRMwkkHtlsNkZJHrdjXRvD4zJdOsLKI")
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

# Initialize an empty list to store conversation history in JSON format
conversation_history = []
iteration_count = 0

# Initial prompt to set the chatbot's tone and style

chat.send_message(prompt)

# Loop to simulate a conversation
while True:
    # Get user input
    user_message = input("YOU: ")
    
    # Send user's message to the bot
    response = chat.send_message(user_message, stream=True, safety_settings={
        'HARASSMENT': 'block_none',
        'HATE_SPEECH': 'block_none',
        'HARM_CATEGORY_HARASSMENT': 'block_none',
        'HARM_CATEGORY_HATE_SPEECH': 'block_none',
        'HARM_CATEGORY_SEXUALLY_EXPLICIT': 'block_none',
        'HARM_CATEGORY_DANGEROUS_CONTENT': 'block_none',
    })
    
    # Collect the bot's full response
    bot_response = "".join([chunk.text for chunk in response])
    print("BOT:", bot_response)
    
    # Append the user-bot exchange to the conversation history list
    conversation_history.append({
        "user_message": user_message,
        "bot_response": bot_response
    })
    
    # Save the conversation history to a JSON file after each interaction
    with open("conversation_history.json", "a") as file:
        json.dump(conversation_history, file, indent=4)
    
    # Increment the iteration count
    iteration_count += 1
    
    # Summarize the conversation and reset chat history every 10 exchanges
    if iteration_count >= 5:
        # Prepare the conversation summary
        conversation_text = "\n".join([
            f"User: {exchange['user_message']} Bot: {exchange['bot_response']}"
            for exchange in conversation_history[-10:]
        ])
        
        summary = model.generate_content(
            f"Summarize this conversation just make it single convo but reduce it but keep the import things dont ingnore those like names and other things : {conversation_text}",
            safety_settings={
                'HARASSMENT': 'block_none',
                'HATE_SPEECH': 'block_none',
                'HARM_CATEGORY_HARASSMENT': 'block_none',
                'HARM_CATEGORY_HATE_SPEECH': 'block_none',
                'HARM_CATEGORY_SEXUALLY_EXPLICIT': 'block_none',
                'HARM_CATEGORY_DANGEROUS_CONTENT': 'block_none',
            }
        )
        
        # Print and store the summary
        summary_text = summary.text
        print("Summary:", summary_text)
        print("-" * 50)
        
        # Append the summary back into the chat history and reset the iteration count
        chat.history = []

        chat.send_message(prompt ,            safety_settings={
                'HARASSMENT': 'block_none',
                'HATE_SPEECH': 'block_none',
                'HARM_CATEGORY_HARASSMENT': 'block_none',
                'HARM_CATEGORY_HATE_SPEECH': 'block_none',
                'HARM_CATEGORY_SEXUALLY_EXPLICIT': 'block_none',
                'HARM_CATEGORY_DANGEROUS_CONTENT': 'block_none',
            } )
        
        # chat.history[1].role = "user"
        # chat.history[1].parts[0].text = summary_text
        
        # chat.history[1].role = "model"
        # chat.history[1].parts[0].text = "Sure this is the chat history for the 10 conversation we had in the past"
        chat.history.append({
            "role": "user",
              "parts": [{"text": summary_text}]
        })
        chat.history.append({
            "role": "model",
            "parts": [{"text": "Sure, this is the chat history for conversations we had in the past. here the convo i the bot am the narrator and im talking about you"}]
        })
        iteration_count = 0  # Reset the counter after summarizing
        print("Full conversation history:", chat.history)
    # Display the current chat history for debugging
    # 
